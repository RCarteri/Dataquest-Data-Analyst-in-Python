## 1. Introducing Data Cleaning ##
'''
The MoMA data set is stored in a list of lists with the variable name moma.

Use the len() function to count how many items (rows) are in the moma list of lists.

Assign the result to a variable called num_rows.
'''
# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

num_rows = len(moma)

## 2. Reading our MoMA Data Set ##
'''
Use the open() function to open the artworks.csv file. Assign the result to opened_file.

Use the reader() function to parse the data from opened_file. Assign the result to read_file.

Use list() to convert read_file into a list of lists. Assign the result to moma.

Use list slicing to remove the column names (the first row) from the moma list of lists.
'''
# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here
opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

## 3. Replacing Substrings with the replace Method ##
'''
We have created a variable, age1, containing the string "I am thirty-one years old".

Use the str.replace() method to create a new string, age2:
    The new string should have the value "I am thirty-two years old".
'''
age1 = "I am thirty-one years old"
age2 = age1.replace('one', 'two')

## 4. Cleaning the Nationality and Gender Columns ##
'''
Use a for loop to loop over the moma list of lists. In each iteration of the loop:

Clean the Nationality column of the data set by:
    Assigning the nationality for each row (found at list index 2 of the row) to a variable.
    Using the str.replace() method to remove the open parentheses (() character.
    Using the str.replace() method to remove the close parentheses ()) character.
    Assigning the cleaned value back to list index 2 of the row.
    
Clean the Gender column of the data set (found at index 5 of the row) by repeating the same technique you used for the Nationality column.
'''
# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again
for row in moma:
    nationality = row[2]
    clean_nationality = nationality.replace('(', '')
    clean_nationality = clean_nationality.replace(')', '')
    row[2] = clean_nationality
    
    gender = row[5]
    clean_gender = gender.replace('(', '')
    clean_gender = clean_gender.replace(')', '')
    row[5] = clean_gender

## 5. String Capitalization ##
'''
Use a loop to iterate over all rows in the moma list of lists. For each row:

Clean the Gender column.
    Assign the value from the Gender column, at index 5, to a variable.
    Make the changes to the value of that variable.
        Use the str.title() method to make the capitalization uniform.
        Use an if statement to check if the value is an empty string. If the value is an empty string, give it the value "Gender Unknown/Other".
    Assign the modified variable back to list index 5 of the row.
    
Clean the Nationality column of the data set (found at index 2) by repeating the same technique you used for the Gender column.
    For missing values in the Nationality column, use the string "Nationality Unknown".
'''
for row in moma:
    gender = row[5]
    gender = gender.title()
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender
    
    nationality = row[2]
    nationality = nationality.title()
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality

## 6. Errors During Data Cleaning ##
'''
We have provided the clean_and_convert() that uses the if statement to bypass missing strings.

Use a for loop to iterate over each row in the moma list of lists. In each iteration:

Assign the BeginDate and EndDate values (at indexes 3 and 4) to variables.

Use the clean_and_convert() function to clean and convert each value.

Assign the converted values back to indexes 3 and 4 so the cleaned values are used in the moma list of lists.
'''
def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    BeginDate = row[3]
    EndDate = row[4]
    row[3] = clean_and_convert(BeginDate)
    row[4] = clean_and_convert(EndDate)

## 7. Parsing Numbers from Complex Strings, Part One ##
'''
Create a function called strip_characters(), which accepts a string argument and:
    Iterates over the bad_chars list, using str.replace() to remove each character.
    Returns the cleaned string.
    
Create an empty list, stripped_test_data.

Iterate over the strings in test_data, and on each iteration:
    Use the function you created earlier to clean the string.
    Append the cleaned string to the stripped_test_data list.
'''
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char, "")
    return string

stripped_test_data = []

for data in test_data:
    data = strip_characters(data)
    stripped_test_data.append(data)
        

## 8. Parsing Numbers from Complex Strings, Part Two ##
'''
The stripped_test_data list, strip_characters() function and bad_chars list are provided for you so you don't have to toggle between screens to remember what they look like.

Create a function called process_date() which accepts a string, and follows the logic we outlined above:
    Checks if the dash character (-) is in the string so we know if it's a range or not.
    If it is a range:
        Splits the string into two strings, before and after the dash character.
        Converts the two numbers to the integer type and then average them by adding them together and dividing by two.
        Uses the round() function to round the average, so values like 1964.5 become 1964.
    If it isn't a range:
        Converts the value to an integer type.
    Finally, returns the value.
    
Create an empty list processed_test_data.

Loop over the stripped_test_data list using your process_date() function. Process the dates and append each processed date back to the processed_test_data list.

Once your code works with the test data, you can then iterate over the moma list of lists. In each iteration:
    Assign the value from the Date column (index 6) to a variable.
    Use the strip_characters() function to remove any bad characters.
    Use the process_date() to convert the date.
    Assign the stripped and processed value back to the row.
'''
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(string):
    if '-' in string:
        split_date = string.split('-')
        data1 = int(split_date[0])
        data2 = int(split_date[1])
        string = round((data1 + data2) / 2)
    else:
        string = int(string)
    
    return string

processed_test_data = []

for data in stripped_test_data:
    data = process_date(data)
    processed_test_data.append(data)
    
print(processed_test_data)

for row in moma:
    date = row[6]
    date = strip_characters(date)
    date = process_date(date)
    row[6] = date