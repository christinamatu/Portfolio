# ✈️ Understanding U.S. Airline Delays: Causes and Patterns

An analysis of U.S. airline delay data to find out **why flights are delayed**, **which airlines and airports are affected most**, and how delays changed during COVID-19.

**Tools:** Python, pandas, NumPy, Matplotlib, Seaborn, scikit-learn

#### Business Problem

Flight delays cost airlines money, frustrate passengers and disrupt connections. This project asks:

> What factors contribute most to airline delays in the United States, and how do their impacts vary across airlines and airports?
> 
#### Dataset

U.S. Airline Delay Statistics (Kaggle, based on Bureau of Transportation Statistics data). Each row is one airline at one airport for one month, with the number of flights, delayed flights (15+ minutes late), cancellations, diversions, and delays by cause.

- **3,351 rows** (3,343 after removing 8 empty rows), 17 airlines, 360 airports
- **Only December 2019 and December 2020**, so the analysis compares these two Decembers rather than looking at seasonal trends

#### Approach

1. Cleaned the data (removed 8 completely empty rows)
2. Created delay, cancellation and diversion rates
3. Used **flight-weighted** delay rates (total delayed flights ÷ total flights) so that small airlines and airports don't distort comparisons
4. Explored delay causes, airlines, airports, COVID-19 impact and correlations
5. Built a Random Forest model using only information known in advance (airline, airport, year, number of flights)

#### Key Findings

**1. Most delay minutes come from late aircraft and airline-controlled issues**

Late aircraft (37.7%) and carrier issues (34.3%) cause about 72% of delay minutes. Weather causes only about 5%, though weather delays are the longest on average (about 123 minutes).

<img width="1389" height="490" alt="image" src="https://github.com/user-attachments/assets/6b23d91b-6295-4735-900c-4c9f95b74d59" />

**2. Delay Rates by Airline**

JetBlue's delay rate was 32.2% in 2019 and 20.4% in 2020. Hawaiian Airlines and Delta had the lowest rates in 2019. Every airline improved in 2020, but by different amounts.

<img width="1031" height="699" alt="image" src="https://github.com/user-attachments/assets/d02eed53-44ac-4390-8f46-68d75a3b6881" />

**3. Newark, San Francisco, Boston and LaGuardia were the most delayed airports**

But airport rankings were **not consistent** between 2019 and 2020 (correlation ≈ 0.09), so with only two Decembers, I can't say any airport is always slow.

<img width="856" height="545" alt="image" src="https://github.com/user-attachments/assets/3a5f9d2f-8397-4422-b799-54283b8e7217" />

**4. COVID-19 Impacts on Flight Delay**

Flights fell by about 41% (625,763 to 371,357) and the delay rate fell from 20.3% to 11.7%. The biggest improvement was in late-aircraft delays (7.7 to 2.4 per 100 flights, which is about 62% of the total drop). With fewer flights, planes had more spare time between trips, so one late arrival was less likely to cause the next delay. NAS delays (airport and air traffic congestion) also fell.

<img width="1589" height="490" alt="image" src="https://github.com/user-attachments/assets/02636ea6-6425-4f49-af81-bfea21522e9a" />

**4. A model using information known in advance explains about 39% of delay-rate variation**

| Model | Avg. error (MAE) | R² |
|---|---|---|
| Always predict the average | 7.80 pts | 0.00 |
| Random Forest (airline, airport, year, flights) | 3.27 pts | 0.77 |

The model's R² is about 0.77 and its average error (MAE) is about 3.3 percentage points, compared to an R² of 0 and an error of 7.8 points for just guessing the average. Moreover, the Pearson r is roughly 0.88, which indicates that the predicted and actual delay rates have a strong positive linear relationship.

<img width="608" height="545" alt="image" src="https://github.com/user-attachments/assets/8f482aad-737a-46e9-9c87-dfd7c353d916" />

#### Recommendations

1. **Add buffer time between flights** on tightly scheduled aircraft, since late-aircraft delay is the biggest cause.
2. **Focus on each airline's main cause** (airline-controlled issues vs. schedule design).
3. **Use weighted delay rates** for airline and airport comparisons.
4. **Collect more data** before using a model to forecast delays.

#### Limitations

- Only two Decembers of data (no full-year seasonality)
- December 2020 was unusual because of COVID-19
- No weather, time-of-day or route information
- Delay causes are reported by the airlines
- Results show associations, not proven causes
