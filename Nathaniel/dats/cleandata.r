library(readr)
library(tidyverse)

math21 <- read_csv("Documents/ProjectsInDS/STAT-456-Final/Nathaniel/dats/math21.csv")

ela21 <- read_csv("Documents/ProjectsInDS/STAT-456-Final/Nathaniel/dats/ela21.csv")


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
# the data is already incredibly wide but we must further widen it to get any use out of the PCT columns

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


wipdats <- schooldata21 %>% mutate(across(contains("PCT"),~colFunc(.x,valueFunction = valFunc)))

wipdats <- wipdats %>% mutate(across(contains("PCT"),~colFunc(.x,valueFunction = periodToNA)))

wipdats <- wipdats %>% mutate(across(contains("PCT"),~colFunc(.x,valueFunction = singlePCTtoRange)))

wideschooldata21 <- wipdats %>% separate_wider_delim(cols = contains("PCT"),delim = "-",names = c("max","min"),names_sep = "_",too_few = "align_start")

write.csv(wideschooldata21,file = "wideschooldata.csv")
