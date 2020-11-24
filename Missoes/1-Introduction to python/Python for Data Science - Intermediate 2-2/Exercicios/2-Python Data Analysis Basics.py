## 1. Reading our MoMA Data Set ##
'''
Use a for loop to iterate over each row in the moma list of lists. Inside the body of the loop:

Assign the value from index 6 (Date) to a variable called date.

Use an if statement to check if date is not equal to "".

If date isn't equal to "", convert it to an integer type using the int() function.

Finally, assign the value back to index 6 in the row.
'''
from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

## 2. Calculating Artist Ages ##
'''
Create an empty list, ages, to store the artist age data.

Use a loop to iterate over the rows in moma.

In each iteration, assign the artwork year (at index 6) to date and artist birth year (at index 3) to birth.
    If the birth date is an int, calculate the age of the artist at the time of creating the artwork, and assign it to the variable age.
    If birth isn't an int type, assign 0 to the variable age.
    Append age to the ages list.
    
Create an empty list final_ages, to store the final age data.

Use a loop to iterate over each age in ages. In each iteration:
    If the age is greater than 20, assign the age to the variable final_age.
    If the age is not greater than 20, assign "Unknown" to the variable final_age.
    Append final_age to the final_ages list.
'''
ages = []
for row in moma:
    date = row[6]
    birth = row[3]
    if type(birth) == int:
        age = date - birth
    else:
        age = 0
    ages.append(age)
    
final_ages = []
for age in ages:
    if age > 20:
        final_age = age
    else:
        final_age = 'Unknown'
    final_ages.append(final_age)

## 3. Converting Ages to Decades ##
'''
Create an empty list, decades, to store the artist decade data.

Iterate over the values in final_ages, and in each iteration:
    If age is "Unknown", assign it to the variable decade
    If age isn't "Unknown":
        Convert the integer value to a string, assigning it to the variable decade.
        Use list slicing to remove the final character of decade.
    Use the + operator to add the substring "0s" to the end of the string decade.
    Append decade to the decades list.
'''
# The final_ages variable is available
# from the previous screen
decades = []
for age in final_ages:
    if age == 'Unknown':
        decade = age
    else:
        decade = str(age)
        decade = decade[:-1]
        decade = decade + '0s'
    decades.append(decade)

## 4. Summarizing the Decade Data ##
'''
Create an empty dictionary, decade_frequency.

Iterate through each item in the decades list. In each iteration:
    If the item is not a key in decade_frequency, add it as a key with a value of 1.
    If the item is a key in decade_frequency, add one to the existing value for that key.
'''
# The decades variable is available
# from the previous screen
decade_frequency = {}
for decade in decades:
    if decade not in decade_frequency:
        decade_frequency[decade] = 1
    else:
        decade_frequency[decade] += 1

## 5. Inserting Variables Into Strings ##
'''
We have provided an artist's name and birth year in the artist and birth_year variables.

Create a template string to insert the artist and birth_year variables into a string, using the format provided above. You may use your choice of the three techniques you learned for specifying which variables goes where.

Use str.format() to insert the two variables into your template string, assigning the result to a variable.

Use the print() function to call that variable.
'''
artist = "Pablo Picasso"
birth_year = 1881

result = "{}'s  birth year is {}".format(artist, birth_year)
print(result)

## 6. Creating an Artist Frequency Table ##
'''
Create an empty dictionary, artist_freq.

Iterate through each item in the moma list of lists. In each iteration:
    Assign the artist's name (column index 1) to the variable artist.
    If artist is not a key in artist_freq, add it as a key with a value of 1.
    If artist is a key in artist_freq, add one to the existing value for that key.
'''
artist_freq = {}
for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1

## 7. Creating an Artist Summary Function ##
'''
Create a function artist_summary() which accepts a single argument, the name of an artist.

The function should print a summary of the artist using the steps below:
    Retrieve the number of artworks from the artist_freq dictionary, and assign it to a variable.
    Create a template string that uses braces ({}) to insert the name and variables into the string, using the format from the diagram above.
    Use str.format() method to insert the artist's name and number of artworks into the string template.
    Use the print() function to display the final string.
    
Use your function to display a summary for the Artist "Henri Matisse".
'''
def artist_summary(artist):
    artworks = artist_freq[artist]
    template = 'There are {} artworks by {} in the data set'.format(artworks, artist)
    print(template)
    
artist_summary('Henri Matisse')
    

## 8. Formatting Numbers Inside Strings ##
'''
Create a template string that will insert the country name and population as shown in the example above.
    The country population should have a precision of two and use a comma separator.
    
Use a for loop to iterate over the pop_millions list of lists and in each iteration:
    Assign the country name and population to two variables.
    Use str.format() to insert the two variables into your template string.
    Use the print() function to display the result of your str.format() call.
'''
pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

for pop in pop_millions:
    country = pop[0]
    population = pop[1]
    result = 'The population of {} is {:,.2f} million'.format(country, population)
    print(result)

## 9. Challenge: Summarizing Artwork Gender Data ##
'''
Create a frequency table for the values in the Gender (row index 5) column.

Loop over each key-value pair in the dictionary. Display a line of output in the format shown above summarizing each pair.
'''
gender_freq = {}
for row in moma:
    gender = row[5]
    if gender not in gender_freq:
        gender_freq[gender] = 1
    else:
        gender_freq[gender] += 1

for gender, freq in gender_freq.items():
    result = "There are {:,} artworks by {} artists".format(freq, gender)
    print(result)