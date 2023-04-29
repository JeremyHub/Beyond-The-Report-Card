# Data Cleaning Document

## Import libraries

library(ggplot2)
library(dplyr)
library(tidyverse)
library(readxl)

## Import data

school_data <- read.csv('AllDatasets/ca_education.csv') # dataset of public K-12 spending by school
ela_metric_data <- read.csv('AllDatasets/ca_edu_metrics.csv') # 2022 Academic Indicator (English Language Arts/Literacy) Data File
physical_fitness_data <- read.csv('AllDatasets/physical_fitness_testing_ca.csv')
science_metric_data <- read.csv('AllDatasets/science_ca_assesment.csv', sep = "^")
stanford_data <- read_csv('AllDatasets/seda_school_pool_gcs_4.1.csv')
ca_school_details <- read_excel("AllDatasets/ca_school_details.xlsx") # CA schools metadata

## Clean CA school metadata

ca_school_details_clean <- ca_school_details %>%
  filter(StatusType == "Active") %>%
  filter(NCESSchool != "No Data") %>%
  filter(School != "No Data") %>%
  mutate(school_id = paste0(NCESDist, NCESSchool))

## Clean Stanford data -- adding 0 in front of school id to match the format of the school dataset

stanford_data_clean <- stanford_data %>% 
  filter(stateabb == 'CA') %>% 
  select(sedasch, sedaschname, fips, stateabb, subcat, subgroup, gradecenter, gap, contains("avg"), -ends_with("se")) %>%
  mutate(standardized_school_id = paste0(0, sedasch))

##  Clean school data

school_data_clean <- school_data %>%
  filter(flag_nerds == 'false') %>%
  filter(flag_f33 != '1')

## Clean ELA data

ela_metric_data_clean <- ela_metric_data %>%
  filter(cds > 0, rtype == 'S') %>% # school record
  select(-color, -box) %>%
  mutate(cds_standardized = as.character(paste0(0, cds)))

colnames(ela_metric_data_clean) <- paste0("ela_data_", colnames(ela_metric_data_clean))


## Clean PE data

physical_fitness_data_clean <- physical_fitness_data %>%
  mutate(cds = as.character(paste0(0, paste0(paste0(CO,DIST),SCHL)))) %>% # add cds identifier
  mutate(cds_standardized = ifelse(nchar(cds) == 13, as.character(paste0(cds,0)), cds)) %>% # there are school codes missing the last 0, this fixes that to match other cds
  filter(Level_Number==1, Table_Number==1, Report_Number==0) %>%
  select(-Level_Number, -Report_Number, -Table_Number, -Line_Number, -ChrtNum)

colnames(physical_fitness_data_clean) <- paste0("PE_data_", colnames(physical_fitness_data_clean))

# ca_school_details_clean %>% filter(str_detect(CDSCode, '0110017124172')) %>% select(CDSCode)


## Clean Science data

science_metrics_clean <- science_metric_data %>%
  mutate(cds = as.character(paste0(0, paste0(paste0(County.Code,District.Code),School.Code)))) %>% # add cds identifier
  mutate(cds_standardized = ifelse(nchar(cds) == 13, as.character(paste0(cds,0)), cds)) %>% # there are school codes missing the last 0, this fixes that to match other cds
  filter(County.Code > 0, Type.ID == 07) %>%
  select(-County.Code, -District.Code, -School.Code, -Filler)

colnames(science_metrics_clean) <- paste0("science_data_", colnames(science_metrics_clean))

# ca_school_details_clean %>% filter(CDSCode == '01611506090419')

## Tables to join: ca school details lj school data on school id, left join stanford data on school id, lj ela on cds, physical fitness on cds, science on cds
## Join keys: metadata vs school data: by=c('school_id'='ncesid'), metadata vs stanford: by=c('school_id'='standardized_school_id'), metadata vs ela: by=c('CDSCode'='ela_data_cds_standardized'), metadata vs pe: by=c('CDSCode'='PE_data_cds_standardized'), metadata vs science: by=c('CDSCode'='science_data_cds_standardized')

merged_table <- left_join(ca_school_details_clean, school_data_clean, by=c('school_id'='ncesid')) %>%
  left_join(., stanford_data_clean, by=c('school_id'='standardized_school_id')) %>%
  left_join(., ela_metric_data_clean, by=c('CDSCode'='ela_data_cds_standardized')) %>%
  left_join(., physical_fitness_data_clean, by=c('CDSCode'='PE_data_cds_standardized')) %>%
  left_join(., science_metrics_clean, by=c('CDSCode'='science_data_cds_standardized'))


save(merged_table,file = 'CombinedDataLongFormat.RData')
