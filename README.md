# Beyond the Report Card: Investigating the Factors that Define Educational Achievement using California as a Case Study

This project was created by [Thu Dang](https://www.linkedin.com/in/thudang24/), [Nathaniel Reimer](https://www.linkedin.com/in/nathaniel-reimer-339542230/), and [Jeremy Hubinger](https://www.linkedin.com/in/jeremy-hubinger/). It contains our analysis of school achievement measures in the state of California. All data is included in this repository. The entire site and analysis can be reconstructed by running `quarto::quarto_render()` in the main directory.

Our analysis used the following packages:
```
library(tidyverse)
library(MetBrewer)
library(sf)
library(rnaturalearth)
library(classInt) #install.packages('classInt')
library(ggspatial) #install.packages('ggspatial')
library(ggthemes) #install.packages('ggthemes')
library(RColorBrewer)
library(patchwork)
library(leaflet)
library(probably) #install.packages('probably')
library(glmnet)
library(tidymodels)
```

Not all are necessary to recreate the report.
