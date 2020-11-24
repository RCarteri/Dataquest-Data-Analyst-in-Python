## 1. Reading CSV files with NumPy ##
'''
Import the NumPy library and assign to the alias np.

Use the numpy.genfromtxt() function to read the nyc_taxis.csv file into NumPy. Assign the result to taxi.

Use the ndarray.shape attribute to assign the shape of taxi to taxi_shape.

Use the variable inspector under the code box to view the taxi ndarray and its shape after running your code.
'''
import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',')
taxi_shape = np.shape(taxi)

## 2. Reading CSV files with NumPy Continued ##
'''
Use the numpy.genfromtxt() function to again read the nyc_taxis.csv file into NumPy, but this time, skip the first row. Assign the result to taxi.

Assign the shape of taxi to taxi_shape.

Use the variable inspector under the code box to view the taxi ndarray and its shape after you have run your code.
'''
import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',', skip_header = True)
taxi_shape = np.shape(taxi)

## 3. Boolean Arrays ##
'''
Use vectorized boolean operations to:
    Evaluate whether the elements in array a are less than 3. Assign the result to a_bool.
    Evaluate whether the elements in array b are equal to "blue". Assign the result to b_bool.
    Evaluate whether the elements in array c are greater than 100. Assign the result to c_bool.
    
Once you've run your code, use the variable inspector below the code box to view each boolean array.
'''
a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = a < 3
b_bool = b == 'blue'
c_bool = c > 100

## 4. Boolean Indexing with 1D ndarrays ##
'''
Calculate the number of rides in the taxi ndarray that are from February:
    Create a boolean array, february_bool, that evaluates whether the items in pickup_month are equal to 2.
    Use the february_bool boolean array to index pickup_month. Assign the result to february.
    Use the ndarray.shape attribute to find the number of items in february. Assign the result to february_rides.
    
Once you have run your code, use the variable inspector to view the number of rides for February.
'''
pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]

## 5. Boolean Indexing with 2D ndarrays ##
'''
Create a boolean array, tip_bool, that determines which rows have values for the tip_amount column of more than 50.

Use the tip_bool array to select all rows from taxi with values tip amounts of more than 50, and the columns from indexes 5 to 13 inclusive. Assign the resulting array to top_tips.
'''
tip_amount = taxi[:,12]
tip_bool = tip_amount > 50
top_tips = taxi[tip_bool, 5:14]

## 6. Assigning Values in ndarrays ##
'''
To help you practice without making changes to our original array, we have used the ndarray.copy() method to make taxi_modified, a copy of our original for these exercises.

The value at column index 5 (pickup_location) of row index 28214 is incorrect. Use assignment to change this value to 1 in the taxi_modified ndarray.

The first column (index 0) contains year values as four digit numbers in the format YYYY (2016, since all trips in our data set are from 2016). Use assignment to change these values to the YY format (16) in the taxi_modified ndarray.

The values at column index 7 (trip_distance) of rows index 1800 and 1801 are incorrect. Use assignment to change these values in the taxi_modified ndarray to the mean value for that column.
'''
# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
taxi_modified[28214, 5] = 1
taxi_modified[:,0] = 16
taxi_modified[1800:1802,7] =  taxi_modified[:,7].mean()

## 7. Assignment Using Boolean Arrays ##
'''
We again used the ndarray.copy() method to make taxi_copy, a copy of our original for this exercise.

Select the fourteenth column (index 13) in taxi_copy. Assign it to a variable named total_amount.

For rows where the value of total_amount is less than 0, use assignment to change the value to 0.
'''
# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()

total_amount = taxi_copy[:,13]
total_amount[total_amount < 0] = 0

## 8. Assignment Using Boolean Arrays Continued ##
'''
We have created a new copy of our taxi dataset, taxi_modified with an additional column containing the value 0 for every row.

In our new column at index 15, assign the value 1 if the pickup_location_code (column index 5) corresponds to an airport location, leaving the value as 0 otherwise by performing these three operations:
    For rows where the value for the column index 5 is equal to 2 (JFK Airport), assign the value 1 to column index 15.
    For rows where the value for the column index 5 is equal to 3 (LaGuardia Airport), assign the value 1 to column index 15.
    For rows where the value for the column index 5 is equal to 5 (Newark Airport), assign the value 1 to column index 15.
'''
# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)
taxi_modified[taxi_modified[:, 5] == 2, 15] = 1
taxi_modified[taxi_modified[:, 5] == 3, 15] = 1
taxi_modified[taxi_modified[:, 5] == 5, 15] = 1

## 9. Challenge: Which is the most popular airport? ##
'''
Using the original taxi ndarray, calculate how many trips had JFK Airport as their destination:
    Use boolean indexing to select only the rows where the dropoff_location_code column (column index 6) has a value that corresponds to JFK. Assign the result to jfk.
    Calculate how many rows are in the new jfk array and assign the result to jfk_count.
    
Calculate how many trips from taxi had Laguardia Airport as their destination:
    Use bhe result to laguardia_count.
    Calculate how many trips from taxi had Newark Airport as their destination:
    Select only the rows where the dropoff_location_code column has a value that corresponds to Newark, and assign the result to newark.
    
Calculate how many rows are in the new newark array and assign the result to newark_count.

After you have run your code, inspect the values for jfk_count, laguardia_count, and newark_count and see which airport has the most dropoffs.
'''
jfk = taxi[taxi[:,6] == 2]
jfk_count = jfk.shape[0]

laguardia = taxi[taxi[:,6] == 3]
laguardia_count = laguardia.shape[0]

newark = taxi[taxi[:,6] == 5]
newark_count = newark.shape[0]

## 10. Challenge: Calculating Statistics for Trips on Clean Data ##
'''
The trip_mph ndarray has been provided for you.

Create a new ndarray, cleaned_taxi, containing only rows for which the values of trip_mph are less than 100.

Calculate the mean of the trip_distance column of cleaned_taxi. Assign the result to mean_distance.

Calculate the mean of the trip_length column of cleaned_taxi. Assign the result to mean_length.

Calculate the mean of the total_amount column of cleaned_taxi. Assign the result to mean_total_amount.
'''
trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
cleaned_taxi = taxi[trip_mph < 100]

mean_distance = cleaned_taxi[:,7].mean()
mean_length = cleaned_taxi[:,8].mean()
mean_total_amount = cleaned_taxi[:,13].mean()