# Introduction
This is a capstone project I worked on for my Google Data Analytics course. In this case study, I performed data analysis for Bellabeat, a high-tech manufacturer of health-focused products for women. I analyzed smart device data to gain insight on how customers are using their smart devices. In order to answer the key business questions, I followed the steps of the data analysis process: Ask, Prepare, Process, Analyze, Share and Act. 

# Scenario
Bellabeat is a relatively small smart device company, but there is potential for the company to grow through analyzing trends in smart device fitness data. Out of five Bellabeat products, one product will be analyzed to gain insight into how customers are using their smart device. The insights discovered will then help guide marketing strategy for the company and an analysis will be presented to the executive team along with business recommendations. 

# Characters 
- Urška Sršen: Bellabeat’s cofounder and Chief Creative Officer
- Sando Mur: Mathematician and Bellabeat’s cofounder; key member of the Bellabeat executive team
- Bellabeat marketing analytics team: A team of data analysts responsible for collecting, analyzing, and reporting data that helps guide Bellabeat’s marketing strategy.

# Products
- Bellabeat app: The Bellabeat app provides users with health data related to their activity, sleep, stress, menstrual cycle, and mindfulness habits. This data can help users better understand their current habits and make healthy decisions. The Bellabeat app connects to their line of smart wellness products.
- Leaf: Bellabeat’s classic wellness tracker can be worn as a bracelet, necklace, or clip. The Leaf tracker connects to the Bellabeat app to track activity, sleep, and stress.
- Time: This wellness watch combines the timeless look of a classic timepiece with smart technology to track user activity, sleep, and stress. The Time watch connects to the Bellabeat app to provide you with insights into your daily wellness.
- Spring: This is a water bottle that tracks daily water intake using smart technology to ensure that you are appropriately hydrated throughout the day. The Spring bottle connects to the Bellabeat app to track your hydration levels.
- Bellabeat membership: Bellabeat also offers a subscription-based membership program for users. Membership gives users 24/7 access to fully personalized guidance on nutrition, activity, sleep, health and beauty, and mindfulness based on their lifestyle and goals.

# About the Company
Urška Sršen and Sando Mur founded Bellabeat, a high-tech company that manufactures health-focused smart products. Sršen used her background as an artist to develop beautifully designed technology that informs and inspires women around the world. Collecting data on activity, sleep, stress, and reproductive health has allowed Bellabeat to empower women with knowledge about their own health and habits. Since it was founded in 2013, Bellabeat has grown rapidly and quickly positioned itself as a tech-driven wellness company for women.

# Ask
- Business task: Analyze Bellabeat smart device data to gain insight on customer marketing strategy
- Key stakeholders: Urška Sršen and Sando Mur

# Prepare 
The data source is FitBit Fitness Tracker Data (CC0: Public Domain, dataset by Mobius) from Kaggle by 30 FitBit participants. 

A good data source is ROCCC, which stands for Reliable, Original, Comprehensive, Current and Cited. 
- Reliability: The dataset is provided by 30 FitBit users who consented to be a part of a survey via Amazon Mechanical Turk from 03/12/2016 to 05/12/2016. 
- Originality: The dataset is by 30 FitBit users who consented to the submission of personal tracker data. 
- Comprehensiveness: Data minute-level output for physical activity, heart rate and sleep monitoring. Although the data tracks factors such as physical activity, heart rate and hours of sleep, the data is only provided by 30 participants which is also only recorded on certain days of the week, which could lead to insufficient data.
- Current: The data has not been updated since 2016. 
- Citation: Unknown 
Overall, it is not a very reliable data source.

The dataset is organized by 18 csv files.  

# Process
#### Loading packages in R Studio and getting to know my data:
``` install.packages("tidyverse")
install.packages("dplyr")
install.packages("ggplot2")

library(tidyverse)
library(dplyr)
library(ggplot2)
library(readr)

daily_activity <- read_csv("Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv")
View(daily_activity)

hourly_calories <- read_csv("Fitabase Data 4.12.16-5.12.16/hourlyCalories_merged.csv")
View(hourly_calories)

hourly_intensities <- read_csv("Fitabase Data 4.12.16-5.12.16/hourlyIntensities_merged.csv")
View(hourly_intensities)

hourly_steps <- read_csv("Fitabase Data 4.12.16-5.12.16/hourlySteps_merged.csv")
View(hourly_steps)

sleep <- read.csv("Fitabase Data 4.12.16-5.12.16/sleepDay_merged.csv")
View(sleep)

weight <- read.csv("Fitabase Data 4.12.16-5.12.16/weightLogInfo_merged.csv")
View(weight)

head(daily_activity)
```
<img width="936" height="155" alt="pic" src="https://github.com/user-attachments/assets/cc75bef4-c0f2-40a4-8ad9-4c7dcc7fd377" />

#### Manipulating and cleaning my data using Pipes:
```new_daily_activity <- daily_activity %>% 
  drop_na() %>% 
  distinct()

new_hourly_calories <- hourly_calories %>% 
  drop_na() %>% 
  distinct()

new_hourly_intensities <- hourly_intensities %>% 
  drop_na() %>% 
  distinct()

new_hourly_steps <- hourly_steps %>% 
  drop_na() %>% 
  distinct()

new_sleep <- sleep %>% 
  drop_na() %>% 
  distinct()

new_weight <- weight %>% 
  drop_na() %>% 
  distinct()
```
There is significant change in data for weight.

#### Data Verification:
```
sum(duplicated(new_daily_activity))
[1] 0
sum(duplicated(new_hourly_calories))
[1] 0
sum(duplicated(new_hourly_steps))
[1] 0
sum(duplicated(new_hourly_intensities))
[1] 0
sum(duplicated(new_sleep))
[1] 0
sum(duplicated(new_weight))
[1] 0
```

#### Formatting dates to weekday: 
```
new_daily_activity <- new_daily_activity %>% 
  mutate( Weekday = weekdays(as.Date(ActivityDate, "%m/%d/%Y")))
```

#### Determining unique participants in each data frame: 
```
n_distinct(new_daily_activity$Id)
[1] 33
n_distinct(new_hourly_calories$Id)
[1] 33
n_distinct(new_hourly_steps$Id)
[1] 33
n_distinct(new_hourly_intensities$Id)
[1] 33
n_distinct(new_sleep$Id)
[1] 24
n_distinct(new_weight$Id)
[1] 2
```
There are exactly 33 participants in all data frame except for 'sleep' and 'weight'. For our sleep data, there are only 24 total participants and for our weight data, there are only 2 participants that gave their body fat percentage data. 

#### Observations in each data frame: 
```
nrow(new_daily_activity)
[1] 940
nrow(new_hourly_calories)
[1] 22099
nrow(new_hourly_steps)
[1] 22099
nrow(new_hourly_intensities)
[1] 22099
nrow(new_sleep)
[1] 410
nrow(new_weight)
[1] 2
```

# Analyze
