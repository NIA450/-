import pandas as pd
import random

# Create a list of unique values in the `whoAmI` column.
unique_values = data['whoAmI'].unique()

# Create a new column for each unique value.
for value in unique_values:
    data[value] = 0

# For each row in the DataFrame, set the value of the new column to 1 if the value in the `whoAmI` column matches the unique value, and 0 otherwise.
for index, row in data.iterrows():
    value = row['whoAmI']
    data.loc[index, value] = 1

# Drop the `whoAmI` column.
data.drop('whoAmI', axis=1, inplace=True)

# Print the resulting DataFrame.
print(data.head())