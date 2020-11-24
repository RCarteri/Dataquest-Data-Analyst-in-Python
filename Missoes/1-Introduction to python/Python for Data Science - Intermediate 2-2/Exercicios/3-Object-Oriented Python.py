## 1. Introduction ##
'''
In the code editor, we have defined one variable of each of the three types we've worked with so far. Follow each of the instructions below, in order.

Use the print() function to display the type of the list l.

Use the print() function to display the type of the string s.

Use the print() function to display the type of the dictionary d.
'''
l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}

print(type(l))
print(type(s))
print(type(d))

## 3. Defining a Class ##
'''
Define a class named MyClass.

Inside the class definition, add a pass statement to avoid a SyntaxError.
'''
class MyClass:
    pass

## 4. Instantiating a Class ##
'''
We provide you with the MyClass class from the previous screen.

Below the class definition, use the MyClass() constructor to create an instance of MyClass. Assign it to a variable named my_instance.

Use the print() and type() built-in functions to print the type of my_instance.
'''
class MyClass:
    pass

my_instance = MyClass()

print(type(my_instance))

## 5. Creating Methods ##
'''
The MyClass class from the previous screen is provided.

Remove the pass statement.

Inside the class, define a method called first_method().

Inside the method, return the string "This is my first method".

Outside of the class, create an instance of MyClass and assign it to a variable name my_instance.
'''
class MyClass:
    def first_method():
        return 'This is my first method'
    
my_instance = MyClass()

## 6. Understanding 'self' ##
'''
The MyClass class from the previous screen is provided.

Modify the first_method() method by adding self as an argument.

Create an instance of the MyClass class. Assign it to the variable name my_instance.

Call my_instance.first_method(). Assign the result to the variable result.
'''
class MyClass:
    
    def first_method(self):
        return "This is my first method"
    
my_instance = MyClass()

result = my_instance.first_method()

## 7. Continue ##
'''
The MyClass class from the previous screen is provided.

Inside the MyClass class, define a new method called return_list() with two arguments:
    self: The self-reference of this instance.
    input_list: A list.
    
Implement the return_list() method so that it returns the given input_list.

Create an instance of the MyClass class, and assign it to the variable name my_instance.

Call the my_instance.return_list() method with the argument [1, 2, 3]. Assign the result to the variable result.
'''
class MyClass:
    
    def first_method(self):
        return "This is my first method"
    
    # Add method here
    def return_list(self, input_list):
        return input_list
    
my_instance = MyClass()

result = my_instance.return_list(1, 2 , 3)
        
## 8. Attributes and the Init Method ##
'''
Define a new class called MyList.

Inside the class, create the __init__() method with two arguments:
    self: The self-reference of this instance.
    initial_data: A list giving the initial values in the list.
    
Inside the __init__() method, store the provided initial_data into self.data.

Outside of the class, instantiate an object of your MyList class, providing the list [1, 2, 3, 4, 5] as the argument. Assign the object to the variable name my_list.

Use the print() function to display the data attribute of my_list.
'''
class MyList:
    def __init__(self, initial_data):
        self.data = initial_data
     
my_list = MyList([1, 2, 3, 4, 5])

print(my_list.data)

## 9. Creating an Append Method ##
'''
The MyList class from the previous screen is provided.

Inside the MyList class, define a new append() method with two arguments:
    self: The self-references to the instance.
    new_item: The new item that we want to add to the list.
    
Implement the append() method so that it appends the provided new_item to the list stored in self.data.

Outside of the class, create an instance of MyList providing the list [1, 2, 3, 4, 5]. Assign it to a variable named my_list.

Print the value of my_list.data.

Use the append() method to append value 6 to my_list.

Print the value of my_list.data. Observe that it now contains the 6 that we added.
'''
class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        
    # Add method here
    def append(self, new_item):
        self.data += [new_item]
        
my_list = MyList([1, 2, 3, 4, 5])
print(my_list.data)
my_list.append(6)
print(my_list.data)

## 10. Creating and Updating an Attribute ##
'''
The MyList class from the previous screen is provided. We've added code in the __init__() method that initializes the list length.

Inside the append() method, add one line of code that updates the length attribute of the list.

Outside of the class, create an instance of MyList providing the list [1, 1, 2, 3, 5]. Assign it to a variable named my_list.

Print the length attribute of my_list.

Use the append() method to append value 8 to my_list.

Print the length attribute of my_list. Observe that it was updated when a new value was added.
'''
class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        # Calculate the initial length
        self.length = 0
        for item in self.data:
            self.length += 1

    def append(self, new_item):
        self.data = self.data + [new_item]
        # Update the length here
        self.length += 1
        
my_list = MyList([1, 2, 3, 4, 5])
print(my_list.length)
my_list.append(8)
print(my_list.length)
class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        # Calculate the initial length
        self.length = 0
        for item in self.data:
            self.length += 1

    def append(self, new_item):
        self.data = self.data + [new_item]
        # Update the length here
class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        # Calculate the initial length
        self.length = 0
        for item in self.data:
            self.length += 1

    def append(self, new_item):
        self.data = self.data + [new_item]
        # Update the length here
        self.length += 1

my_list = MyList([1, 1, 2, 3, 5])
print(my_list.length)

my_list.append(8)
print(my_list.length)