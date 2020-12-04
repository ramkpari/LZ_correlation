library(rmarkdown)
library(tidyverse)
library(knitr)
library(plyr)
library(dplyr)


# File loading. To be replaced with one big file with data from all participants universally.


data = read_csv("data/7_new_STLI_2020_Nov_23_1853.csv")


# Correct answer verification through string comparison

data_2 = data %>% mutate(correct_answer_verification = case_when(data$correct_answer == data$key_resp.keys ~ 1,
                                                                 data$correct_answer != data$key_resp.keys ~ 0 ) )


# Summarising the data with for stats analysis 


summary = data_2 %>% group_by(stimulus_type,frequency) %>% dplyr::summarise(mean = mean(correct_answer_verification),n = n())
                                                                 
