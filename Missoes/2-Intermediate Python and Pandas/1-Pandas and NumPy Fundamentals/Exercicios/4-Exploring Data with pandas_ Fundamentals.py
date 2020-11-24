## 1. Introduction to the Data ##
'''
We've already read the data set into a pandas dataframe and assigned it to a variable named f500.

Use the DataFrame.head() method to select the first 10 rows in f500. Assign the result to f500_head.

Use the DataFrame.info() method to display information about the dataframe.
'''
f500_head = f500.head(10)
f500.info()

## 2. Vectorized Operations ##
'''
Subtract the values in the rank column from the values in the previous_rank column. Assign the result to rank_change.
'''
rank_change =f500['previous_rank'] - f500['rank']

## 3. Series Data Exploration Methods ##
'''
Use the Series.max() method to find the maximum value for the rank_change series. Assign the result to the variable rank_change_max.

Use the Series.min() method to find the minimum value for the rank_change series. Assign the result to the variable rank_change_min.
'''
rank_change =  f500["previous_rank"] - f500["rank"]
rank_change_max = rank_change.max()
rank_change_min = rank_change.min()

## 4. Series Describe Method ##
'''
Return a series of descriptive statistics for the rank column in f500.
    Select the rank column. Assign it to a variable named rank.
    Use the Series.describe() method to return a series of statistics for rank. Assign the result to rank_desc.
    
Return a series of descriptive statistics for the previous_rank column in f500.
    Select the previous_rank column. Assign it to a variable named prev_rank.
    Use the Series.describe() method to return a series of statistics for prev_rank. Assign the result to prev_rank_desc.
'''
rank = f500['rank']
rank_desc = rank.describe()
prev_rank = f500['previous_rank']
prev_rank_desc = prev_rank.describe()

## 5. Method Chaining ##
'''
Use Series.value_counts() and Series.loc to return the number of companies with a value of 0 in the previous_rank column in the f500 dataframe. Assign the results to zero_previous_rank.
'''
zero_previous_rank = f500['previous_rank'].value_counts().loc[0]

## 6. Dataframe Exploration Methods ##
'''
Use the DataFrame.max() method to find the maximum value for only the numeric columns from f500 (you may need to check the documentation). Assign the result to the variable max_f500.
'''
max_f500 = f500.max(numeric_only=True)

## 7. Dataframe Describe Method ##
'''
Return a dataframe of descriptive statistics for all of the numeric columns in f500. Assign the result to f500_desc.
'''
f500_desc = f500.describe()

## 8. Assignment with pandas ##
'''
The company "Dow Chemical" has named a new CEO. Update the value where the row label is Dow Chemical and for the ceo column to Jim Fitterling in the f500 dataframe.
'''
f500.loc['Dow Chemical', 'ceo'] = 'Jim Fitterling'

## 9. Using Boolean Indexing with pandas Objects ##
'''
Create a boolean series, motor_bool, that compares whether the values in the industry column from the f500 dataframe are equal to "Motor Vehicles and Parts".

Use the motor_bool boolean series to index the country column. Assign the result to motor_countries.
'''
motor_bool = f500['industry'] == "Motor Vehicles and Parts"
motor_countries = f500.loc[motor_bool, 'country']

## 10. Using Boolean Arrays to Assign Values ##
'''
Use boolean indexing to update values in the previous_rank column of the f500 dataframe:
    There should now be a value of np.nan where there previously was a value of 0.
    It is up to you whether you assign the boolean series to its own variable first, or whether you complete the operation in one line.
    
Create a new pandas series, prev_rank_after, using the same syntax that was used to create the prev_rank_before series.
'''
import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
f500.loc[f500['previous_rank'] == 0, 'previous_rank'] = np.nan
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()

## 11. Creating New Columns ##
'''
Add a new column named rank_change to the f500 dataframe by subtracting the values in the rank column from the values in the previous_rank column.

Use the Series.describe() method to return a series of descriptive statistics for the rank_change column. Assign the result to rank_change_desc.
'''
f500['rank_change'] = f500['previous_rank'] - f500['rank']
rank_change_desc = f500['rank_change'].describe()

## 12. Challenge: Top Performers by Country ##
'''
Create a series, industry_usa, containing counts of the two most common values in the industry column for companies headquartered in the USA.

Create a series, sector_china, containing counts of the three most common values in the sector column for companies headquartered in the China.
'''
industry_usa = f500["industry"][f500["country"] == "USA"].value_counts().head(2)
sector_china = f500["sector"][f500["country"] == "China"].value_counts().head(3)