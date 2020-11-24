## 1. Lists ##

'''
Store the second row ('Instagram', 0.0, 'USD', 2161558, 4.5) as a list in a variable named row_2.

Store the third row ('Clash of Clans', 0.0, 'USD', 2130805, 4.5) as a list in a variable named row_3.
'''
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

## 2. Indexing ##

'''
In the code editor, you can already see the lists for the first three rows.
The fourth element in each list describes the number of ratings an app has received. Retrieve this fourth element from each list, and then find the average value of the retrieved numbers.
    Assign the fourth element from the list row_1 to a variable named ratings_1. Don't forget that the indexing starts at 0.
    Assign the fourth element from the list row_2 to a variable named ratings_2.
    Assign the fourth element from the list row_3 to a variable named ratings_3.
    Add the three numbers retrieved together and save the sum to a variable named total.
    Divide the sum (now saved in the variable total) by 3 to get the average number of ratings for the first three rows. Assign the result to a variable named average.
'''
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
ratings_1 = row_1[3]
ratings_2 = row_2[3]
ratings_3 = row_3[3]
total = ratings_1 + ratings_2 + ratings_3
average = total / 3

## 3. Negative Indexing ##

'''
The last element in each list shows the average rating of each application.
Retrieve the ratings for the first three rows, and then find the average value of all the ratings retrieved.
    Assign the last element from the list row_1 to a variable named rating_1. Try to take advantage of negative indexing.
    Assign the last element from the list row_2 to a variable named rating_2.
    Assign the last element from the list row_3 to a variable named rating_3.
    Add the three ratings together and save the sum to a variable named total_rating.
'''
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
rating_1 = row_1[-1]
rating_2 = row_2[-1]
rating_3 = row_3[-1]
total_rating = rating_1 + rating_2 + rating_3
average_rating = total_rating / 3

## 4. Retrieving Multiple List Elements ##

'''
For Facebook, Instagram, and Pandora — Music & Radio, isolate the rating data in separate lists. Each list should contain the name of the app, the rating count, and the user rating. Don't forget that indexing starts at 0.
    For Facebook, assign the list to a variable named fb_rating_data.
    For Instagram, assign the list to a variable named insta_rating_data.
    For Pandora — Music & Radio, assign the list to a variable named pandora_rating_data.

Compute the average user rating for Facebook, Instagram, and Pandora — Music & Radio using the data you stored in fb_rating_data, insta_rating_data, and pandora_rating_data.
    You'll need to add the ratings together first, and then divide the total by the number of ratings.
    Assign the result to a variable named avg_rating.
    As a side note, we could calculate the average rating here a little bit better using the weighted mean — we'll learn about the weighted mean in the statistics courses.
'''
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

fb_rating_data = [row_1[0], row_1[3], row_1[-1]]
insta_rating_data = [row_2[0], row_2[3], row_2[-1]]
pandora_rating_data = [row_5[0], row_5[3], row_5[-1]]
avg_rating = (fb_rating_data[2] + insta_rating_data[2] + pandora_rating_data[2]) / 3

## 5. List Slicing ##

'''
Select the first four elements from row_1 using a list slicing syntax shortcut. Assign the output to a variable named first_4_fb.

Select the last three elements from row_1 using a list slicing syntax shortcut. Assign the output to a variable named last_3_fb.

From row_5, select the list slice ['USD', 1126879] using a list slicing syntax shortcut. Assign the output to a variable named pandora_3_4.
'''
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
first_4_fb = row_1[:4]
last_3_fb = row_1[-3:]
pandora_3_4 = row_5[2:4]

## 6. List of Lists ##

'''
In the code editor, we've already stored the five rows as lists in separate variables. Group together the five lists in a list of lists. Assign the resulting list of lists to a variable named app_data_set.

Compute the average rating of the apps by retrieving the right data points from the app_data_set list of lists.
    The rating is the last element of each row. You'll need to sum up the ratings and then divide by the number of ratings.
    Assign the result to a variable named avg_rating.
'''
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
app_data_set = [row_1, row_2, row_3, row_4, row_5]
avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] + app_data_set[2][-1] + app_data_set[3][-1] + app_data_set[4][-1]) / 5
 

## 7. Opening a File ##
'''
Open the AppleStore.csv file and store it as list of lists.

Open the file using the open() command. Save the output to a variable named opened_file.

Read in the opened file using the reader() command (we've already imported reader() for you from the csv module). Save the output to a variable named read_file.

Transform the read-in file to a list of lists using the list() command. Save the list of lists to a variable named apps_data.

Explore apps_data. You could:
    Print its length using the len() command
    Print the first row (the row describing column names)
    Print the second and the third row (try to use list slicing here)
'''
from csv import reader
opened_file = open('CSVs/AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)
print(len(apps_data))
print(apps_data[0])
print(apps_data[1:2])

## 8. Repetitive Processes ##

'''
Use the new technique we've learned to print all the rows in the app_data_set list of lists.
    Essentially, you'll need to translate this pattern into Python syntax: for each list in the app_data_set variable, print that list.
    Don't forget about indentation.
'''
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

for each_list in app_data_set:
    print(each_list)

## 9. For Loops ##

'''
Compute the average app rating for the apps stored in the app_data_set variable.

Initialize a variable named rating_sum with a value of zero outside the loop body.

Loop (iterate) over the app_data_set list of lists. For each of the five iterations of the loop (for each row in app_data_set):

Extract the rating of the app and store it to a variable named rating. The rating is the last element of each row.

Add the value stored in rating to the current value of the rating_sum.

Outside the loop body, divide the rating sum (stored in rating_sum) by the number of ratings to get an average value. Store the result in a variable named avg_rating.
'''
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

rating_sum = 0
for each_row in app_data_set:
    rating = each_row[-1]
    rating_sum += rating
    
avg_rating = rating_sum/len(app_data_set)

## 10. The Average App Rating ##

'''
Compute the average app rating for all the 7,197 apps stored in the data set.

Initialize a variable named rating_sum with a value of zero.

Loop through the apps_data[1:] list of lists (make sure you don't include the header row). For each of the 7,197 iterations of the loop (for each row in apps_data[1:]):
    Extract the rating of the app and store it to a variable named rating (the rating has the index number 7). Make sure you convert the rating value from a string to a float using the float() command.
    Add the value stored in rating to the current value of the rating_sum.
    
Divide the rating sum (stored in rating_sum) by the number of ratings to get an average value. Store the result in a variable named avg_rating.
'''
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = 0
for data in apps_data[1:]:
    rating = float(data[7])
    rating_sum += rating
    
avg_rating = rating_sum/len(apps_data[1:])

## 11. Alternative Way to Compute an Average ##

'''
Using the new technique we've learned, compute the average app rating for all of the 7,197 apps stored in our data set.

Initialize an empty list named all_ratings.

Loop through the apps_data[1:] list of lists (make sure you don't include the header row). For each of the 7,197 iterations of the loop:
    Extract the rating of the app and store it to a variable named rating (the rating has the index number 7). Make sure you convert the rating value from a string to a float.
    Append the value stored in rating to the list all_ratings.
    
Compute the sum of all ratings using the sum() command.

Divide the sum of all ratings by the number of ratings, and assign the result to a variable named avg_rating.
'''
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

all_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    all_ratings.append(rating)
    
avg_rating = sum(all_ratings) / len(all_ratings)