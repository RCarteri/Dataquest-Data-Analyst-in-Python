## 2. Introduction to Ndarrays ##
'''
Execute the instructions below in the script.py code box on the right.

Import numpy and assign to the alias np.

Create a NumPy ndarray from the list [10, 20, 30]. Assign the result to the variable data_ndarray.

Click 'Run Code' to run your code and get feedback.

Click 'Submit Answer' to check your answer.
'''
import numpy as np
data_ndarray = np.array([10, 20, 30])

## 4. NYC Taxi-Airport Data ##
'''
In the script.py code box on the right, we have used Python's csv module to import the nyc_taxis.csv file and convert it to a list of lists containing float values.

Add a line of code using the numpy.array() constructor to convert the converted_taxi_list variable to a NumPy ndarray.

Assign the result to the variable name taxi.
'''
import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
taxi = np.array(converted_taxi_list)

## 5. Array Shapes ##
'''
Throughout all of our Dataquest missions, variables we created in previous screens are available.

Assign the shape of taxi to taxi_shape. Print the result.
'''
taxi_shape = taxi.shape
print(taxi_shape)

## 6. Selecting and Slicing Rows and Items from ndarrays ##
'''
From the taxi ndarray:

Select the row at index 0. Assign it to row_0.
Select every column for the rows at indexes 391 to 500 inclusive. Assign them to rows_391_to_500.
Select the item at row index 21 and column index 5. Assign it to row_21_column_5.
'''
row_0 = taxi[0]
rows_391_to_500 = taxi[391:501]
row_21_column_5 = taxi[21, 5]

## 7. Selecting Columns and Custom Slicing ndarrays ##
'''
From the taxi ndarray:

Select every row for the columns at indexes 1, 4, and 7. Assign them to columns_1_4_7.

Select the columns at indexes 5 to 8 inclusive for the row at index 99. Assign them to row_99_columns_5_to_8.

Select the rows at indexes 100 to 200 inclusive for the column at index 14. Assign them to rows_100_to_200_column_14.
'''
columns = [1, 4, 7]
columns_1_4_7 = taxi[:, columns]

row_99_columns_5_to_8 = taxi[99,5:9]

rows_100_to_200_column_14 = taxi[100:201,14]


## 8. Vector Math ##
'''
Use vector addition to add fare_amount and fees_amount. Assign the result to fare_and_fees.

After you have run your code, use the variable inspector below the code box to inspect the variables.
'''
fare_amount = taxi[:,9]
fees_amount = taxi[:,10]

fare_and_fees = fare_amount + fees_amount

## 9. Vector Math Continued ##
'''
Use vector division to divide trip_distance_miles by trip_length_hours. Assign the result to trip_mph.

After you have run your code, use the variable inspector below the code box to inspect the contents of the new trip_mph variable.
'''
trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour

trip_mph = trip_distance_miles / trip_length_hours



## 10. Calculating Statistics For 1D ndarrays ##
'''
Use the ndarray.max() method to calculate the maximum value of trip_mph. Assign the result to mph_max.

Use the ndarray.mean() method to calculate the average value of trip_mph. Assign the result to mph_mean.
'''
mph_min = trip_mph.min()

mph_max = trip_mph.max()

mph_mean = trip_mph.mean()

## 12. Calculating Statistics For 2D ndarrays ##
'''
We've already assigned the first five rows of taxi to taxi_first_five and the first four columns in the table above to fare_components.
Check that the sum of each row in fare_components equals the value in the total_amount column.

Use the ndarray.sum() method to calculate the sum of each row in fare_components. Assign the result to fare_sums.

Extract the 14th column in taxi_first_five. Assign to fare_totals.

Print fare_totals and fare_sums. Use the variable inspector to verify the results match.
'''
# we'll compare against the first 5 rows only
taxi_first_five = taxi[:5]
# select these columns: fare_amount, fees_amount, tolls_amount, tip_amount
fare_components = taxi_first_five[:,9:13]

fare_sums = fare_components.sum(axis = 1)
fare_totals = taxi_first_five[:,13]
print(fare_totals, fare_sums)