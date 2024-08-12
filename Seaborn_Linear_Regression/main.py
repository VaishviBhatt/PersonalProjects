import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

#notebook presentation
pd.options.display.float_format = '{:,.2f}'.format

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#read data
data = pd.read_csv('cost_revenue_dirty.csv')

#Convert the USD_Production_Budget, USD_Worldwide_Gross,
# and USD_Domestic_Gross columns to a numeric format by removing $ signs and ,

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget',
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']

for col in columns_to_clean:
    for char in chars_to_remove:
        # Replace each character with an empty string
        data[col] = data[col].astype(str).str.replace(char, "")
    # Convert column to a numeric data type
    data[col] = pd.to_numeric(data[col])
    data.head()

#Challenge:

#What is the average production budget of the films in the data set?
#What is the average worldwide gross revenue of films?
#What were the minimums for worldwide and domestic revenue?
#Are the bottom 25% of films actually profitable or do they lose money?
#What are the highest production budget and highest worldwide gross revenue of any film?
#How much revenue did the lowest and highest budget films make?

data.describe()
data[data.USD_Production_Budget == 1100.00]
data[data.USD_Production_Budget == 425000000.00]

#How many films grossed $0 domestically (i.e., in the United States)?
# What were the highest budget films that grossed nothing?

zero_domestic = data[data.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
zero_domestic.sort_values('USD_Production_Budget', ascending=False)

#How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally?
zero_worldwide = data[data.USD_Worldwide_Gross == 0]
print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
zero_worldwide.sort_values('USD_Production_Budget', ascending=False)

international_releases = data.loc[(data.USD_Domestic_Gross == 0) &
                                  (data.USD_Worldwide_Gross != 0)]
print(f'Number of international releases: {len(international_releases)}')
international_releases.head()

# Use the .query() function to accomplish the same thing. Create a subset for international
# releases that had some worldwide gross revenue, but made zero revenue in the United States.

international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}')
international_releases.tail()

#Identify which films were not released yet as of the time of data collection (May 1st, 2018).
#How many films are included in the dataset that have not yet had a chance to be screened in the box office?
#Create another DataFrame called data_clean that does not include these films.


# Date of Data Collection
scrape_date = pd.Timestamp('2018-5-1')
future_releases = data[data.Release_Date >= scrape_date]
print(f'Number of unreleased movies: {len(future_releases)}')
future_releases

# exclude future releases
data_clean = data.drop(future_releases.index)

# difference is 7 rows
data.shape[0] - data_clean.shape[0]

#What is the percentage of films where the production costs exceeded the worldwide gross revenue?
money_losing = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
len(money_losing)/len(data_clean)
money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
money_losing.shape[0]/data_clean.shape[0]



#Seaborn for Data Viz: Bubble Charts

#revenue in billions vs budget in 100 million
plt.figure(figsize=(8,4), dpi=200)
ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     hue='USD_Worldwide_Gross', # change colour
                     size='USD_Worldwide_Gross',) # change size of dot

ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions',)
# set styling on a single chart
with sns.axes_style('darkgrid'):
  ax = sns.scatterplot(data=data_clean,
                       x='USD_Production_Budget',
                       y='USD_Worldwide_Gross',
                       hue='USD_Worldwide_Gross',
                       size='USD_Worldwide_Gross')

  ax.set(ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel='Revenue in $ billions',
        xlabel='Budget in $100 millions')

plt.show()

#Create a column in data_clean that has the decade of the release
dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year
decades = years//10*10
data_clean['Decade'] = decades

#Separate the "old" (before 1969) and "New" (1970s onwards) Films
old_films = data_clean[data_clean.Decade <= 1960]
new_films = data_clean[data_clean.Decade > 1960]
old_films.describe()
old_films.sort_values('USD_Production_Budget', ascending=False).head()

#How much global revenue does our model estimate for a film with a budget of $350 million?
budget = 350000000
regression = LinearRegression()
revenue_estimate = regression.intercept_[0] + regression.coef_[0,0]*budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')