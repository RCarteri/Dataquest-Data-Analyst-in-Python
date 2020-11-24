## 1. If Statements ##
'''
Complete the code in the editor to find the average rating for free apps.

Inside the for loop:

Assign the price of an app as a float to a variable named price. The price is the fifth element in each row (don't forget that the index starts at 0).

If price == 0.0, append the value stored in rating to the free_apps_ratings list using the list_name.append() command (note the free_apps_ratings is already defined in the code editor). Be careful with indentation.

Outside the for loop body, compute the average rating of free apps. Assign the result to a variable named avg_rating_free. The ratings are stored in the free_apps_ratings list.
'''
# INITIAL CODE
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    # Complete the code from here
    price = float(row[4])
    if price == 0.0:
        free_apps_ratings.append(rating)
        
avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)

## 2. Booleans ##
'''
In the code editor, we've already initialized the variable a_price with a value of 0. Transcribe the following sentences into code by making use of if statements:

If a_price is equal to 0, then print the string 'This is free' (remember to use the == operator for equality).

If a_price is equal to 1, then print the string 'This is not free'.
'''
a_price = 0
if a_price == 0:
    print("This is free")
    
if a_price == 1:
    print("This is not free")

## 3. The Average Rating of Non-free Apps ##
'''
Modify the existing code in the editor on the right to compute the average rating of non-free apps.

Change the name of the empty list from free_apps_ratings to non_free_apps_ratings (the list we defined before the for loop).

Change the condition if price == 0.0 to account for the fact that we now want to isolate only the ratings of non-free apps.

Change free_apps_ratings.append(rating) to make sure the ratings are appended to the new list non_free_apps_ratings.

Compute the average value by summing up the values in non_free_apps_ratings and dividing by the length of this list. Assign the result to avg_rating_non_free.

Optional exercise: Inspect the value of avg_rating_non_free and compare the average with that of free apps (the average rating of free apps is approximately 3.38 — we computed it in the first screen). Can we use the average values to say that free apps are better than non-free apps, or vice versa?
'''
# INITIAL CODE
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price != 0.0:
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

## 4. The Average Rating of Gaming Apps ##
'''
Following the same techniques we used in the diagram above, compute the average rating of non-gaming apps.

Initialize an empty list named non_games_ratings.

Loop through the apps_data list of lists (make sure you don't include the header row). For each iteration of the loop:
    Assign the rating of the app as a float to a variable named rating (the index number of the rating column is 7).
    Assign the genre of the app to a variable named genre (index number 11).
    If the genre is not equal to 'Games', append the rating to the non_games_ratings list.
    
Compute the average rating of non-gaming apps, and assign the result to a variable named avg_rating_non_games.

Optional exercise: Compare the average rating of gaming apps (3.69) with that of non-gaming apps. Why do you think we see this difference?
'''
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    
    if genre != "Games":
        non_games_ratings.append(rating)
        
avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)

## 5. Multiple Conditions ##
'''
Complete the code in the editor to compute the average rating of free gaming apps.

Inside the for loop, append the rating to the free_games_ratings list if the price is equal to 0.0 and the genre is equal to 'Games'.

Outside the for loop, compute the average rating of free gaming apps. Assign the result to a variable named avg_rating_free_games.
'''
# INITIAL CODE
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    # Complete code from here
    if price == 0.0 and genre == "Games":
        free_games_ratings.append(rating)
        
avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)

## 6. The or Operator ##
'''
Complete the code in the editor to compute the average rating of the apps whose genre is either "Social Networking" or "Games."

Inside the for loop, append the rating to the games_social_ratings list if the genre is either 'Social Networking' or 'Games'.

Outside the for loop, compute the average rating of the apps whose genre is either "Social Networking" or "Games," and assign the result to a variable named avg_games_social.
'''
# INITIAL CODE
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    # Complete code from here
    if genre == "Social Networking" or genre == "Games":
        games_social_ratings.append(rating)
        
avg_games_social = sum(games_social_ratings) / len(games_social_ratings)

## 7. Combining Logical Operators ##
'''
Compute the average rating of non-free apps whose genre is either "Social Networking" or "Games."
    Assign the result to a variable named avg_non_free.
    We'll try to solve this exercise without any guidance. You may feel a bit stumped at first, but we've practiced the steps needed to solve this kind of exercise several times. Essentially, the code is almost identical to what we used to extract the ratings for free gaming or social networking apps.
'''
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price == 0:
        free_games_social_ratings.append(rating)
        
avg_free = sum(free_games_social_ratings) / len(free_games_social_ratings)

# Non-free apps (average)
non_free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        non_free_games_social_ratings.append(rating)
        
avg_non_free = sum(non_free_games_social_ratings) / len(non_free_games_social_ratings)


## 8. Comparison Operators ##
'''
Compute the average rating of the apps that have a price greater than $9.

    Using a for loop, isolate the ratings of all the apps that have a price greater than $9. When you iterate over apps_data, make sure you don't include the header row.
    Find the average value of these ratings and assign the result to a variable named avg_rating.
   
Find out how many apps have a price greater than $9 and assign the result to a variable named n_apps_more_9. You can use the list of ratings from the previous question to find the answer.

Find out how many apps have a price less than or equal to $9 and assign the result to a variable named n_apps_less_9. The list of ratings from the first question can help you find a quick answer.
'''
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
lista = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price >= 9.0:
        lista.append(rating)
        
avg_rating = sum(lista) / len(lista) 

n_apps_more_9 = len(lista)
n_apps_less_9 = len(apps_data[1:]) - n_apps_more_9

## 9. The else Clause ##
'''
Complete the code in the editor to label each app as "free" or "non-free" depending on its price.
    Inside the for loop:
        If the price of the app is 0.0, then label the app as "free" by appending the string 'free' to the current iteration variable.
        Else, label the app "non-free" by appending the string 'non-free' to the current iteration variable. Make sure you don't write 'non_free' instead of 'non-free'.
        By adding labels to the end of each row, we basically created a new column. Name this column "free_or_not" by appending the string 'free_or_not' to the first row of the apps_data data set. Make sure this is done outside the for loop.
        
Print the header row and the first five rows to see some of the changes we made.
'''
# INITIAL CODE
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append("free")
    else:
        app.append("non-free")

apps_data[0].append("free_or_not")

for app in apps_data[0:5]:
    print(app)

## 10. The elif Clause ##
'''
Complete the code in the editor to label each app as "free," "affordable," "expensive," or "very expensive." Inside the loop:

    If the price of the app is 0, label the app as "free" by appending the string 'free' to the current iteration variable.
    If the price of the app is greater than 0 and less than 20, label the app as "affordable". For efficiency purposes, use an elif clause.
    If the price of the app is greater or equal to 20 and less than 50, label the app as "expensive". For efficiency purposes, use an elif clause.
    If the price of the app is greater or equal to 50, label the app as "very expensive". For efficiency purposes, use an elif clause.
    
Name the newly created column "price_label" by appending the string 'price_label' to the first row of the apps_data data set.

Inspect the header row and the first five rows to see some of the changes you made.
'''
# INITIAL CODE
opened_file = open('CSVs/AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append("free")
    elif price > 0 and price < 20:
        app.append("affordable")
    elif price >= 20 and price < 50:
        app.append("expensive")
    elif price >= 50:
        app.append("very expensive")
   
apps_data[0].append("price_label")

for app in apps_data[0:6]:
    print(app)