<img width="589" height="173" alt="bellabeat" src="https://github.com/user-attachments/assets/d0372207-34b2-439b-ab8e-a5e2ec95208a" />

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
The data source is [FitBit Fitness Tracker Data](https://www.kaggle.com/datasets/arashnic/fitbit) (CC0: Public Domain, dataset by Mobius) from Kaggle by 30 FitBit participants. 

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
#### Determining the relationship between smart device usage per day of the week: 
```
new_daily_activity$Weekday <- factor(new_daily_activity$Weekday, levels = c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))

ggplot(data=new_daily_activity)+ 
  geom_bar(mapping=aes(x=factor(new_daily_activity$Weekday, levels = c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")), fill=Weekday))+
  labs(title="Usage Per Day of the Week", x="Weekday")
```
<img width="740" height="391" alt="analyze" src="https://github.com/user-attachments/assets/f9a3ae58-d4dd-42c5-baac-99ff5c49b36c" />

According to the bar graph above, Tuesdays have the most smart device usage by 30 FitBit participants with a number of 150 count. Coming in very close are Wednesdays and Thursdays with a count value of exactly 150 and a count value of a little less than 150, respectively. 

#### Relationship between total steps taken and calories burned per weekday: 
```
ggplot(data=new_daily_activity)+
  geom_smooth(mapping=aes(x=TotalSteps, y=Calories, color=Weekday))+
  facet_wrap(~Weekday)+
  labs(title="Correlation between Total Steps and Calories Per Day of Week")
```
<img width="740" height="389" alt="data" src="https://github.com/user-attachments/assets/c4ce6d8e-beaf-4798-96ad-f95806ada4cc" />

The correlation between total steps taken and calories burned are linear on most days except for Sunday despite having the most total steps of over 35,000 steps. On Sunday, there seems to be a plateau in total calories burned after 25,000 steps. On the other hand, Saturday has the most calories burned at 4,500 calories over a course of 30,000 total steps. 

#### A different perspective on total steps vs. calories burned:
```
ggplot(data=new_daily_activity, aes(x=TotalSteps, y=Calories, color=Weekday))+
  geom_point()+
  geom_smooth()+
  labs(title="Calories Burned vs. Total Steps Taken")
```
<img width="740" height="387" alt="data2" src="https://github.com/user-attachments/assets/578809dc-56b8-4588-bdc9-8795f7b7afbc" />

#### Summary of total steps and calories: 
```
new_daily_activity %>%  
  select(TotalSteps,
         Calories) %>%
  summary()
```
<img width="341" height="158" alt="totalstepscalories" src="https://github.com/user-attachments/assets/1cf8b4ee-37a6-4d48-a2fd-7354b47887d1" />

As expected, the graphs above shows that as the more steps are being taken, the more calories are burned with the exception of some outliers. The maximum total steps taken are 36,019 steps whereas the minimum steps taken are 0 steps and the maximum calories burned is 4,900 calories and the minimum calories burned are 0 calories. 

#### Calories burned at very active minutes: 
```
ggplot(data=new_daily_activity, aes(x=VeryActiveMinutes, y=Calories, color=VeryActiveMinutes))+
  geom_point()+
  geom_smooth()+
  labs(title="Calories Burned at Very Active Minutes")
```
<img width="740" height="398" alt="8b5f01_82e123a6950e4ceaaefe3fe2060bc1e9~mv2" src="https://github.com/user-attachments/assets/7b16268a-1d45-413e-9d61-920a11f70da9" />

#### Calories burned at sedentary active minutes: 
```
ggplot(data=new_daily_activity, aes(x=SedentaryMinutes, y=Calories, color=SedentaryMinutes))+
  geom_point()+
  geom_smooth()+
  labs(title="Calories Burned at Sedentary Active Minutes")
```
<img width="740" height="398" alt="fsbgf" src="https://github.com/user-attachments/assets/ab12122c-6a5f-4ce4-9a99-8fed021d2bb5" />

#### Summary of calories burned and the average values of very active and sedentary minutes:
```
new_daily_activity %>% 
  summarise(Avg_VeryActiveMinutes=mean(VeryActiveMinutes), 
            Avg_SedentaryMinutes=mean(SedentaryMinutes), 
            Max_Calories=max(Calories),
            Min_Calories=min(Calories))
```
<img width="682" height="58" alt="ajhdkjhgs" src="https://github.com/user-attachments/assets/e7a287cc-509d-4d62-b38d-98cc4b4cdcb5" />

When looking at the graphs for the calories burned at various minutes, we can see that there is a linear correlation between calories burned at more active minutes. We also see that majority of the users are burning between the 1,500 to the 3,000 calories range in less than 50 minutes. However, at less active minutes, a significant number of users are taking more than 1,000 minutes to burn less than 3,000 calories. The average very active minutes is 21.2 minutes and the average sedentary active minutes is 991.0 minutes. The maximum calories burned is 4,900 calories and the minimum calories burned is 0 calories. Overall, participants are still burning high calories regardless of how long it takes to burn them. 

#### Relationship between total minutes asleep and total minutes spent in bed:
```
ggplot(data=new_sleep, aes(x=TotalTimeInBed, y=TotalMinutesAsleep))+
  geom_point()+
  geom_smooth()+
  labs(title="Total Minutes Asleep in Bed")
```
<img width="740" height="398" alt="dfkjdsbf" src="https://github.com/user-attachments/assets/2b0246fc-69c2-4552-adc2-a7313189ae87" />

#### Relationship between total minutes asleep and total minutes spent in bed by Day of Week:
```
sleep_weekdays <- new_sleep %>% 
  mutate( Weekday = weekdays(as.Date(SleepDay, "%m/%d/%Y")))

sleep_weekdays$Weekday <- factor(sleep_weekdays$Weekday, levels = c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))

ggplot(data=sleep_weekdays, aes(x=TotalTimeInBed, y=TotalMinutesAsleep, color=Weekday))+
  geom_point()+
  geom_smooth()+
  facet_wrap(~Weekday)+
  labs(title="Total Minutes Asleep in Bed by Day of Week")
```
<img width="740" height="385" alt="dhfkjshdfjk" src="https://github.com/user-attachments/assets/14e7ae56-f2f1-4da8-9f5f-49252456ac5f" />

#### Summary of total sleep records, total minutes asleep and total time spent in bed:
```
new_sleep %>%  
  select(TotalSleepRecords, TotalMinutesAsleep, TotalTimeInBed) %>%
  summary()
```
<img width="523" height="138" alt="ejdhfkjdsf" src="https://github.com/user-attachments/assets/f8cbdc54-1ba1-4820-888a-3cba46e27fda" />

As expected, the more time spent being in bed, the more sleep participants get. The maximum number of sleeps recorded is 3 with a minimum number of sleeps recorded being 1. The maximum total minutes asleep is 796 minutes (13.3 hours) and the minimum total minutes asleep is 58.0 minutes. The maximum total time in bed is 961 minutes (16.0 hours) and the minimum total time in bed is 61.0 minutes. This data suggests that some participants may have a busier schedule than others leading to shorter time spent in bed and an overall shorter sleep time. 

# Share and Act
I have shared my presentation on Tableau. Click [here](https://public.tableau.com/app/profile/christina.matu/viz/BellaBeatCaseStudy_17091678864490/Story1) to learn more about my findings. 

#### Key takeaways: 
- Taking more steps leads to more calories being burned
- Higher calories can be burned regardless of workout intensity levels (highly active vs. sedentary)
- More time spent in bed overall means more time spent sleeping 

<img width="740" height="548" alt="tableau" src="https://github.com/user-attachments/assets/68eb004a-9d5a-467d-a7db-cdfbf7e482f4" />
