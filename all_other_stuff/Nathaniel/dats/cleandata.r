library(readr)
library(tidyverse)
library("rstudioapi")

setwd(dirname(getActiveDocumentContext()$path))

math21 <- read_csv("math21.csv")

ela21 <- read_csv("ela21.csv")

nerdschoolreport <- read_csv("nerdschoolreport.csv")

math21 <- math21 %>% filter(STNAM == "CALIFORNIA") %>% 
  rename("MTH_NUMVALID"="NUMVALID") %>%
  rename("MTH_PCTPROF"="PCTPROF") %>%
  select(-SUBJECT)

ela21 <- ela21 %>% filter(STNAM == "CALIFORNIA") %>% 
  rename("ELA_NUMVALID"="NUMVALID") %>%
  rename("ELA_PCTPROF"="PCTPROF") %>%
  select(-SUBJECT)

data21 <- full_join(ela21,math21,by=c("SCHOOL_YEAR","GRADE","CATEGORY","LEAID","ST_SCHID","STNAM","FIPST","ST_LEAID","LEANM","NCESSCH","DATE_CUR","SCHNAM"))

schooldata21 <- data21 %>% pivot_wider(names_from = c(CATEGORY,GRADE),values_from = c(ELA_NUMVALID,ELA_PCTPROF,MTH_NUMVALID,MTH_PCTPROF))

valFunc <- function(val) {
  if (is.na(val)) {
    return(".")
  } else if (str_detect(val,"GE")) {
    return(paste0(str_extract(val,"[:digit:]+"),"-100"))
  } else if (str_detect(val,"GT")) {
    return(paste0(str_extract(val,"[:digit:]+"),"-100"))
  } else if (str_detect(val,"LT")) {
    return(paste0("0-",str_extract(val,"[:digit:]+")))
  } else if (str_detect(val,"LE")) {
    return(paste0("0-",str_extract(val,"[:digit:]+")))
  } else if (val=="PS") {
    return(NA)
  } else {return(val)}
}

periodToNA <- function(val) {
  if (is.na(val)) {
    return(val)
  } else if (val == ".") {
    return(NA)
  } else {return(val)}
}

singlePCTtoRange <- function(val) {
  if (is.na(val)) {
    return(val)
  } else if (!str_detect(val,"-")) {
    return(paste(val,val,sep="-"))
  } else (return(val))
}


colFunc <- function(col, valueFunction) {  # TODO: There is probably a better way to do this...
  sapply(col, valueFunction)
}

wipdats <- data21 %>% mutate(across(contains("PCT"),~colFunc(.x,valueFunction = valFunc)))

wipdats <- wipdats %>% mutate(across(contains("PCT"),~colFunc(.x,valueFunction = periodToNA)))

wipdats <- wipdats %>% mutate(across(contains("PCT"),~colFunc(.x,valueFunction = singlePCTtoRange)))

wideschooldata21 <- wipdats %>% separate_wider_delim(cols = contains("PCT"),delim = "-",names = c("min","max"),names_sep = "_",too_few = "align_start")

write.csv(wideschooldata21,file = "wideschooldata.csv")

# School Summary Stats

schoolsummary <- schooldata21 %>% mutate(across(contains("NUMVALID"),~.x/ELA_NUMVALID_ALL_00))

schoolsummary <- schoolsummary %>% left_join(nerdschoolreport, by = c("NCESSCH"="ncesid")) %>% select(-contains("PCT"))

write.csv(schoolsummary,file="schoolsummary.csv")
                                        
