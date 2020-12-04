library(rmarkdown)
library(tidyverse)
library(knitr)
library(plyr)
library(dplyr)
library(pracma)

# File loading. To be replaced with one big file with data from all participants universally.


data = read_csv("data\x.csv")

# strcmp test
if (strcmp(c("yes", "no"), c("yes", "no")) == 1){
  print('aa')
}

