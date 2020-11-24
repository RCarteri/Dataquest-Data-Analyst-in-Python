## 1. Functions ##
'''
Compute the sum of a_list (already defined in the code editor) without using sum().
    Initialize a variable named sum_manual with a value of 0.
    Loop through a_list, and for each iteration add the current number to sum_manual.
    
Print sum_manual and sum(a_list) to check whether the values are the same.
'''
a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

sum_manual = 0

for item in a_list:
    sum_manual += item
    
print(sum_manual, sum(a_list))

## 2. Built-in Functions ##
'''
Generate a frequency table for the ratings list, which is already initialized in the code editor.
    Start by creating an empty dictionary named content_ratings.
    Loop through the ratings list. For each iteration:
        If the rating is already in content_ratings, then increment the frequency of that rating by 1.
        Else, initialize the rating with a value of 1 inside the content_ratings dictionary.
        
Print content_ratings.
'''
ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings = {}
for item in ratings:
    if item in content_ratings:
        content_ratings[item] += 1
    else:
        content_ratings[item] = 1

print(content_ratings)
        

## 3. Creating Our Own Functions ##
'''
Recreate the square() function above and compute the square for numbers 10 and 16.
    Assign the square of 10 to a variable named squared_10.
    Assign the square of 16 to a variable named squared_16.
 '''
def square(num):
    return num * num

squared_10 = square(10)
squared_16 = square(16)

## 4. The Structure of a Function ##
'''
Create a function named add_10() that:
    Takes a number as the input (name the input variable as you wish).
    Adds the integer 10 to that number.
    Returns the result of the addition.
    
Use the add_10() function to:
    Add 10 to the number 30. Assign the result to a variable named add_30.
    Add 10 to the number 90. Assign the result to a variable named add_90.
'''
def add_10(num):
    return num + 10

add_30 = add_10(30)
add_90 = add_10(90)

## 5. Parameters and Arguments ##
'''
Recreate the square() function by omitting the variable assignment step inside the function's body.

Without typing out the name of the parameter, use the new square() function to compute the square of the numbers 6 and 11.
    Assign the square of 6 to a variable named squared_6. 
    Assign the square of 11 to a variable named squared_11.
 '''
def square(num):
    return num * num

squared_6 = square(6)
squared_11 = square(11)

## 6. Extract Values From Any Column ##
'''
Write a function named extract() that can extract any column you want from the apps_data data set.
    The function should take in the index number of a column as input (name the parameter as you want).
    
Inside the function's definition:
    Create an empty list.
    Loop through the apps_data data set (excluding the header). Extract only the value you want by using the parameter (which is expected to be an index number).
    Append that value to the empty list.
    Return the list containing the values of the column.
    
Use the extract() function to extract the values in the prime_genre column. Store them in a variable named genres. The index number of this column is 11.
'''
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(column):
    list = []
    for item in apps_data[1:]:
        param = item[column]
        list.append(param)
    return list

genres = extract(11)

## 7. Creating Frequency Tables ##
'''
Write a function named freq_table() that generates a frequency table for any list.
    The function should take in a list as input.
    Inside the function's body, write code that generates a frequency table for that list and stores the table in a dictionary.
    Return the frequency table as a dictionary.
    
Use the freq_table() function on the genres list (already defined from the previous screen) to generate the frequency table for the prime_genre column. Store the frequency table to a variable named genres_ft.

Feel free to experiment with the extract() and freq_table() functions to easily create frequency tables for any column you want.
'''
# CODE FROM THE PREVIOUS SCREEN
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

def freq_table(list):
    li = {}
    for item in list:
        if item in li:
            li[item] += 1
        else:
            li[item] = 1
    return li
genres = extract(11)
genres_ft = freq_table(genres)
    

## 8. Writing a Single Function ##
'''
Write a function named freq_table() that generates a frequency table for any column in our iOS apps data set.
    The function should take the index number of a column in as an input (name the parameter as you want).
    Inside the function's body:
    Loop through the apps_data data set (don't include the header row) and extract the value you want by using the parameter (which is expected to be an index number).
    Build the frequency table as a dictionary.
    The function should return the frequency table as a dictionary.
    
Use the freq_table() function to generate a frequency table for the user_rating column (the index number of this column is 7). Store the table in a variable named ratings_ft.
'''
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(column):
    frequency_table = {}
    for item in apps_data[1:]:
        value = item[column]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
    return frequency_table

ratings_ft = freq_table(7)



## 9. Reusability and Multiple Parameters ##
'''
Update the current freq_table() function to make it more reusable.
    The function should take in two inputs this time: a data set and the index of a column (name the parameters as you want).
    Inside the function's body:
        Loop through the data set using that parameter which is expected to be a data set (a list of lists). For each iteration, select the value you want by using the parameter which is expected to be an index number.
        Build the frequency table as a dictionary.
    The function should return the frequency table as a dictionary.
    
Use the updated freq_table() function to generate a frequency table for the user_rating column (the index number of this column is 7). Store the table in a variable named ratings_ft.
'''
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table
ratings_ft= freq_table(apps_data, 7)

## 10. Keyword and Positional Arguments ##
'''
Use the freq_table() function to generate frequency tables for the cont_rating, user_rating, and prime_genre columns.
    Use positional arguments when you generate the table for the cont_rating column (index number 10). Assign the table to a variable named content_ratings_ft.
    Use keyword arguments for the user_rating column (index number 7) following the order (data_set, index). Assign the table to a variable named ratings_ft.
    Use keyword arguments for the prime_genre column (index number 11) following the order (index, data_set). Assign the table to a variable named genres_ft.
'''
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

content_ratings_ft = freq_table(apps_data, 10)
ratings_ft = freq_table(data_set = apps_data, index = 7)
genres_ft = freq_table(index = 11, data_set = apps_data)


## 11. Combining Functions ##
'''
Write a function named mean() that computes the mean for any column we want from a data set.
    The function should take in two inputs: a data set and an index value.
    Inside the body of the mean() function, use the extract() function to extract the values of a column into a separate list, and then compute the mean of the values in that list using find_sum() and find_length().
    The function should return the mean of the column.
    
Use the mean() function to compute the mean of the price column (index number 4). Assign the result to a variable named avg_price.
'''
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    list = extract(data_set, index)
    return find_sum(list) / find_length(list)

avg_price = mean(apps_data, 4)
    

## 12. Debugging Functions ##
'''
The code we provided in the code editor has several bugs (errors). Run the code, and then use the information provided in the tracebacks to debug the code.

Select all lines of code and press ctrl + / (PC) or ⌘ + / (Mac) to uncomment it so you can modify it.

For a demo of how this keyboard shortcut works, see this help article.

To understand what the bug is, read the general description of the error.

To understand where the bug is, follow the red arrows.
    You'll see the arrows are represented as ---> or ^.
    
Note that there's more than one bug in the code we wrote. Once you debug an error, you'll get another error. This doesn't mean you're not making progress, on the contrary — you're closer to debugging the code completely.
'''
def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)