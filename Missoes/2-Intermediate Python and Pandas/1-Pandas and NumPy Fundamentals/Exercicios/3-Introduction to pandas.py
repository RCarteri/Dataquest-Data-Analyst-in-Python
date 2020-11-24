## 2. Introduction to the Data ##
'''
Use Python's type() function to assign the type of f500 to f500_type.

Use the DataFrame.shape attribute to assign the shape of f500 to f500_shape.
'''
import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None
f500_type = type(f500)
f500_shape = f500.shape

## 3. Introducing DataFrames ##
'''
Just like in the previous missions, the f500 variable we created on the previous screen is available to you here.

Use the head() method to select the first 6 rows. Assign the result to f500_head.

Use the tail() method to select the last 8 rows. Assign the result to f500_tail.
'''
f500_head = f500.head(6)
f500_tail = f500.tail(8)

## 4. Introducing DataFrames Continued ##
'''
Use the DataFrame.info() method to display information about the f500 dataframe.
'''
f500.info()

## 5. Selecting a Column From a DataFrame by Label ##
'''
Select the industry column. Assign the result to the variable name industries.

Use Python's type() function to assign the type of industries to industries_type.
'''
industries = f500['industry']
industries_type = type(industries)

## 7. Selecting Columns From a DataFrame by Label Continued ##
'''
Select the country column. Assign the result to the variable name countries.

In order, select the revenues and years_on_global_500_list columns. Assign the result to the variable name revenues_years.

In order, select all columns from ceo up to and including sector. Assign the result to the variable name ceo_to_sector.
'''
countries = f500['country']
revenues_years = f500[['revenues','years_on_global_500_list']]
ceo_to_sector = f500.loc[:,'ceo':'sector']

## 8. Selecting Rows From a DataFrame by Label ##
'''
By selecting data from f500:

Create a new variable toyota, with:
    Just the row with index Toyota Motor.
    All columns.
    
Create a new variable, drink_companies, with:
    Rows with indicies Anheuser-Busch InBev, Coca-Cola, and Heineken Holding, in that order.
    All columns.
    
Create a new variable, middle_companies with:
    All rows with indicies from Tata Motorsto Nationwide, inclusive.
    All columns from rank to country, inclusive.
'''
toyota = f500.loc['Toyota Motor']
drink_companies = f500.loc[['Anheuser-Busch InBev', 'Coca-Cola', 'Heineken Holding']]
middle_companies = f500.loc['Tata Motors':'Nationwide','rank':'country']

## 10. Value Counts Method ##
'''
We've already saved a selection of data from f500 to a dataframe named f500_sel.

Find the counts of each unique value in the country column in the f500_sel dataframe.
    Select the country column in the f500_sel dataframe. Assign it to a variable named countries.
    Use the Series.value_counts() method to return the value counts for countries. Assign the results to country_counts.
'''
countries = f500_sel['country']
country_counts = countries.value_counts()

## 11. Selecting Items from a Series by Label ##
'''
From the pandas series countries_counts:

Select the item at index label India. Assign the result to the variable name india.

In order, select the items with index labels USA, Canada, and Mexico. Assign the result to the variable name north_america.
'''
countries = f500['country']
countries_counts = countries.value_counts()
india = countries_counts['India']
north_america = countries_counts[['USA','Canada','Mexico']]

## 12. Summary Challenge ##
'''
By selecting data from f500:

Create a new variable big_movers, with:
    Rows with indices Aviva, HP, JD.com, and BHP Billiton, in that order.
    The rank and previous_rank columns, in that order.
    
Create a new variable, bottom_companies with:
    All rows with indices from National Gridto AutoNation, inclusive.
    The rank, sector, and country columns.
'''
big_movers = f500.loc[['Aviva','HP','JD.com','BHP Billiton'],['rank','previous_rank']]
bottom_companies = f500.loc['National Grid':'AutoNation', ['rank','sector','country']]