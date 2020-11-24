## 1. Interfering with the Built-in Functions ##

'''
Write a function named max() that takes in a list but just returns the string "No max value returned".

Use the max() function on the list a_list. Assign the result to a variable named max_val_test_0.

Print max_val_test_0. Observe how the function returned "No max value returned" instead of 10.

Run the code del max to delete the max() function you wrote. This will allow you to use the built-in max() function again.
'''
a_list = [1, 8, 10, 9, 7]
print(max(a_list))

def max(value):
    return "No max value returned"
    
max_val_test_0 = max(a_list)
print(max_val_test_0)

del max

print(max(a_list))

## 3. Default Arguments ##
'''
Edit the open_dataset() function and add the name of iOS apps data set ('CSVs/AppleStore.csv') as a default argument for the file_name parameter.

Without passing in any argument, use the open_dataset() function to open the AppleStore.csv file. Assign the data set to a variable named apps_data.

Inspect the apps_data data set after you run the code to confirm that everything went as expected. You can try to print the first few rows or just use the variable inspector of the code editor.
'''
# INITIAL CODE
def open_dataset(file_name='CSVs/AppleStore.csv'):
    
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data

apps_data = open_dataset()

for i in apps_data[:6]:
    print(i)

## 4. The Official Python Documentation ##

'''
Find the documentation of the round() function (you may remember we used round() in the second mission). Here's a link to the search page.

Read all the documentation of the round() function.

By using the right parameters and arguments:
    Round 3.43 to one decimal point. Assign the result to one_decimal.
    Round 0.23321 to two decimal points. Assign the result to two_decimals.
    Round 921.2225227 to five decimal points. Assign the result to five_decimals.
'''
one_decimal = round(3.43, 1)
two_decimals = round(0.23321, 2)
five_decimals = round(921.2225227, 5)

## 5. Multiple Return Statements ##
'''
Add an extra parameter to the open_dataset() function (already written in the code editor) such that it only returns data sets without header rows.
    If the parameter indicates that data set has a header row, the function removes the header row before returning the data set.
    Else (if the parameter doesn't indicate that data set doesn't have a header row), the function returns the data set as it is.
    It's up to you whether you use default arguments or not.
    
Use the updated open_dataset() function to open the AppleStore.csv file — recall that the AppleStore.csv data set has a header row. Assign the data set to a variable named apps_data.
'''
# INITIAL CODE
def open_dataset(file_name='CSVs/AppleStore.csv', header = True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    if header:
        return data[1:]
    return data

apps_data = open_dataset()

## 6. Returning Multiple Variables ##
'''
Edit the open_dataset() function (already written in the code editor) such that:
    If the data set has a header, the function returns separately both the header and the rest of the data set.
    Else (if there's no header), the function returns the entire data set.
    
    Use the updated open_dataset() function to open the AppleStore.csv file, which has a header row.
    Assign the result to a variable named all_data.
    Use tuple indexing to extract the header and the rest of the data set from the all_data tuple.
        Assign the header to a variable named header.
        Assign the rest of the data set to a variable named apps_data.
'''
# INITIAL CODE
def open_dataset(file_name='CSVs/AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[0], data[1:]
    else:
        return data
    
all_data = open_dataset()
header = all_data[0]
apps_data = all_data[1]

## 7. More About Tuples ##
'''
Use the open_dataset() function to open the AppleStore.csv file, which has a header row.

Do the variable assignment step in a single line of code.
    Assign the header to a variable named header.
    Assign the rest of the data set to a variable named apps_data.
'''
def open_dataset(file_name='CSVs/AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
    
   
apps_data, header = open_dataset()

## 8. Functions
'''
Rewrite the print_constant() function above.

Call the print_constant() function to make sure x = 3.14 gets executed.

Print the variable x using the print() function.
    What do you notice about the output?
    This may be totally unexpected, and we'll explain why this happens in the next screen.
'''
def print_constant():
    x = 3.14
    print(x)
    
print(x)

## 9.
'''
Create a function named exponential() that takes in a single parameter named x.
    Inside the function definition:
        Assign 2.72 to a variable named e.
        Print e.
    The function should return e to the power of x.
    Call the exponential() function with an argument of 5. Assign the result to a variable named result.
    Hypothesize what you should see if you printed e in the main program after calling the exponential() function. Print e to confirm or reject your hypothesis.
    
Create a new function named divide() which doesn't take in any parameter, and then call the function.
    Inside the function definition:
        Print the a_sum variable.
        Print the length variable.
    The function should return the result of the division between a_sum and length.
    Call the divide() function. Try to assign the result to a variable named result_2. Before running the code, hypothesize whether we'll get an error or not.
'''
e = 'mathematical constant'
a_sum = 1000
length = 50

def exponential(x):
    e = 2.72
    print(e)
    return e ** x

result = exponential(5)
print(e)

def divide():
    print(a_sum)
    print(length)
    return a_sum / length
result_2 = divide()