## 1. Saving Values ##

'''
Save the result of (42 - 11) * 22 to result.
Print result.
'''
result = (42 - 11) * 22
print(result)

## 2. Variables ##

'''
Store the value 15 in a variable named a_value.
Store the result of (25 - 7) * 17 to a variable named a_result.
Using the print() command, display the following:
    The value stored in the a_value variable.
    The result of adding 12 to the variable a_result.
    The result of adding a_value to a_result.
'''
a_value = 15
a_result = (25 - 7) * 17
print(a_value)
print(a_result + 12)
print(a_value + a_result)

## 3. Variable Names ##

'''
In the code editor on the right, we attempted to store 34000 in a variable named old-income, and 40000 in a variable named new income. But both of these variable names cause syntax errors, so we commented-out the code.
    Change the variable name old-income to old_income to prevent a syntax error.
    Change the variable name new income to new_income to prevent a syntax error.
    Remove the # from each line so that the code will run, then run the code.
'''
# INITIAL CODE
old_income = 34000
new_income = 40000

## 4. Updating Variables ##

'''
Update the variable income by adding 6000 to its current value. The variable income is already shown in the code editor on the right.
Print income.
'''
income = 34000 + 6000
print(income)

## 5. Syntax Shortcuts ##

'''
Assign a value of 20 to a variable named variable_1.
Assign a value of 20 to a variable named variable_2.
Update the value of variable_2 by adding 10 to its current value. You can take advantage of the += operator.
Update the value of variable_1 by multiplying its current value by 4. You can take advantage of the *= operator.
Display variable_1 and variable_2 using print().
'''
variable_1 = 20
variable_2 = 20
variable_2 += 10
variable_1 *= 4
print(variable_1)
print(variable_2)

## 6. Integers and Floats ##

'''
Assign the integer 10 to a variable named variable_1.
Assign the float 2.5 to a variable named variable_2.
Update the value of variable_1 by adding the float 6.5 to its current value. You can use the += operator.
Update the value of variable_2 by multiplying its current value by the integer 2. You can use the *= operator.
Display variable_1 and variable_2 using print().
'''
variable_1 = 10
variable_2 = 2.5
variable_1 += 6.5
variable_2 *= 2
print(variable_1)
print(variable_2)

## 7. Conversion Between Types ##

'''
Assign the value 13.9 to a variable named variable_a.
Assign the value 2.8 to a variable named variable_b.
Round variable_a using the round() command, and assign back the rounded value to variable_a.
Convert variable_b from a float to an integer using the int() command, and assign back the converted value to variable_b.
Display variable_a and variable_b using the print() command.
'''
variable_a = 13.9
variable_b = 2.8
variable_a = round(variable_a)
variable_b = int(variable_b)
print(variable_a)
print(variable_b)

## 8. Strings ##

'''
Assign the string Pandora - Music & Radio to a variable named app_name.
Assign the string 4.0 to a variable named average_rating. Make sure you don't mistake a string for a float.
Assign the string 1724546 to a variable named total_ratings. Make sure you don't mistake a string for an integer.
Assign the string free to a variable named price.
Display the app_name variable using print().
'''
app_name = "Pandora - Music & Radio"
average_rating = "4.0"
total_ratings = '1724546'
price = 'free'
print(app_name)

## 9. Escaping Special Characters ##

'''
Assign the string Facebook's new motto is "move fast with stable infra." to a variable named motto.
    Notice there's a . character at the end of Facebook's new motto is "move fast with stable infra." — you'll need to include the . character in your answer.
Display the variable motto using print() — displaying motto is required for answer checking.
'''
motto = 'Facebook\'s new motto is "move fast with stable infra."'
print(motto)

## 10. String Operations ##

'''
Assign the string Facebook's rating is to a variable named facebook.
Assign the float 3.5 to a variable named fb_rating.
Convert fb_rating from a float to a string using the str() command, and assign the converted value to a new variable named fb_rating_str.
Concatenate the strings stored in facebook and fb_rating_str to form the string Facebook's rating is 3.5.
    Assign the concatenated string to a variable named fb.
    You'll need to add a space character between Facebook's rating is and 3.5 to avoid ending up with the string Facebook's rating is3.5.
Display the fb variable using print() — this is required for answer checking.
'''
facebook = "Facebook's rating is"
fb_rating = 3.5
fb_rating_str = str(fb_rating)
fb = (facebook + ' ' +  fb_rating_str)
print(fb)