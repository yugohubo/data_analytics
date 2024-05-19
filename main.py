import pandas as pd

# DATA READ

df = pd.read_csv("country_vaccination_stats.csv") # Read data from csv
df.sort_values(by='daily_vaccinations', ascending=True, inplace=True)  # Sorting

df2 = df.copy() # so we don't alter the base dataframe for reusability

# To find the minimum amount of daily vaccinations and make them a groupby series to pull data from
countries = df2.groupby("country")["daily_vaccinations"]
series = countries.min()
series.fillna(value=0.0,inplace=True) # fill grouped country min Nan values with 0


# Define a function for lambda
def fill_na(row, grouped_series):
    if pd.isna(row['daily_vaccinations']):
        return grouped_series[row['country']] # Return the value from the grouped series' min values
    else:
        return row['daily_vaccinations'] # If not Nan just fill the same value

# Apply the function to each row in the DataFrame
df2['daily_vaccinations'] = df2.apply(lambda row: fill_na(row, series), axis=1)

print(pd.isna(df2).describe()) # check if any Nan remains

df2.sort_values(by='country',ascending=True,inplace=True)
df2.to_csv('output.csv')

print(df2)

# Sum of vaccinations by date
date_finder = df2.groupby('date')['daily_vaccinations']
date_sums = date_finder.sum()
print(date_sums)

# Top Three Countries with the most Vaccinations Median

country_medians = df2.groupby('country')['daily_vaccinations'].median()
country_medians_df = pd.DataFrame(country_medians)
country_medians_df.sort_values(by = 'daily_vaccinations',ascending = False, inplace= True)
print(country_medians_df.head(3))


