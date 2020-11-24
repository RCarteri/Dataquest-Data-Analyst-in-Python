## 1. Introduction ##
'''
Use the open() function to open the CSV file potus_visitors_2015.csv

Use the reader() function to read the opened file.

Use the list() function to convert the read file into a list of lists format.
    Assign the list of lists to the variable name potus.
    Remove the first row of the data set, which contains the column names.
'''
from csv import reader
opened_file = open('potus_visitors_2015.csv')
read_file = reader(opened_file)
potus = list(read_file)
potus_head = potus[0]
potus = potus[1:]

## 3. The Datetime Module ##
'''
Import the datetime module with the alias dt
'''
import datetime as dt

## 4. The Datetime Class ##
'''
Import the datetime class using the alias dt.

Instantiate a datetime object representing midnight on June 16, 1911. Assign the object to the variable name ibm_founded.

Instantiate a datetime object representing 8:17 p.m. on July 20, 1969. Assign the object to the variable name man_on_moon.
'''
import datetime as dt
ibm_founded = dt.datetime(1911, 6, 16)
man_on_moon = dt.datetime(1969, 7, 20, 20, 17)

## 5. Using Strptime to Parse Strings as Dates ##
'''
Create a string date_format that specifies the format of the appt_start_date column:
    The format of the app_start_date column is {month}/{day}/{two digit year} {hour 24hr time}:{minute}.
    Substitute each of the values inside braces with the appropriate strftime code from the table above.
    
Iterate over each row in the potus list of lists:
    Assign the appt_start_date column, found at index 2 of each row, to a variable.
    Use the datetime.strptime() constructor to convert the variable from a string to a datetime object, using the date_format string you created earlier.
    Assign the datetime object back to index 2 of the row.
'''
# The `potus` list of lists is available from
# the earlier screen where we created it
date_format = '%m/%d/%y %H:%M'

for row in potus:
    data = row[2]
    row[2] = dt.datetime.strptime(data, date_format)

## 6. Using Strftime to format dates ##
'''
Initialize an empty dictionary, visitors_per_month.

Iterate over the rows in the potus list of lists. In each iteration:
    Assign the datetime object from the appt_start_date column (index 2) to a variable.
    Call the datetime.strftime() method on the appt_start_date object to create a string in the format "January, 1901".
        The format code for the name of the month is %B
        The format code for a four-digit year is %Y.
    If the string is not a key in visitors_per_month, add it as a key with a value of 1.
    Otherwise, add 1 to the existing value for that key.
'''
visitors_per_month = {}
for row in potus:
    data = row[2]
    obj = dt.datetime.strftime(data, '%B, %Y')
    if obj not in visitors_per_month:
        visitors_per_month[obj] = 1
    else:
        visitors_per_month[obj] += 1
        

## 7. The Time Class ##
'''
Instantiate an empty appt_times list.

Iterate over each row in the potus list of lists. For each iteration:
    Assign the datetime object stored at index value 2 to a variable.
    Create a time object from the datetime object.
    Append the time object to the appt_times list.
'''
appt_times = []
for row in potus:
    var = row[2]
    time = var.time()
    appt_times.append(time)

## 8. Comparing time objects ##
'''
The appt_times list is available from the previous screen.

Assign the earliest appointment time from the appt_times list to the variable min_time.

Assign the latest appointment time from the appt_times list to the variable max_time.
'''
min_time = min(appt_times)
max_time = max(appt_times)

## 9. Calculations with Dates and Times ##
'''
Calculate the time between dt_2 and dt_1 and assign the result to answer_1.

Add 56 days to dt_3 and assign the result to answer_2.

Subtract 3600 seconds from dt_4 and assign the result to answer_3.
'''
dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(days = 56)
answer_3 = dt_4 - dt.timedelta(seconds = 3600)

## 10. Summarizing Appointment Lengths ##
'''
We have provided code that converts the appt_end_date to datetime objects.

Instantiate an empty dictionary for our frequency table, appt_lengths.

Loop over each row in potus, and:
    Assign the values for appt_start_date (index 2) and appt_end_date (index 3) to variables.
    Subtract appt_start_date from appt_end_date to calculate the length of the appointment, length.
    If length is not a key in appt_lengths, add it as a key with a value of 1.
    If length is a key in appt_lengths, add 1 to the existing value of that key.
    
Calculate the minimum key in appt_lengths and assign the result to min_length.

Calculate the maximum key in appt_lengths and assign the result to max_length.
'''
for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date
   
appt_lengths = {}
for row in potus:
    start_date = row[2]
    end_date = row[3]
    length = end_date - start_date
    if length not in appt_lengths:
        appt_lengths[length] = 1
    else:
        appt_lengths[length] += 1
        
min_length = min(appt_lengths)
max_length = max(appt_lengths)