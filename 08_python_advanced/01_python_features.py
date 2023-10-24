# ++++++++ Creating a function that creates a class. ++++++++
def make_class(x):
    """ 'Class Constructor' """
    class Dog:
        def __init__(self, name):
            self.name = name
        
        def print_value(self):
            print(x)
    
    return Dog


# Getting the class
cls = make_class(10)
print('Printing the class returned from function make_class():')
print(cls)

# Instantiating an object of the class
obj = cls(name="Object")
print('Printing the value passed to make_class(x):')
obj.print_value()


# ++++++++ Defining a function inside a loop ++++++++
print('Printing the range with a function inside the loop:')
for n in range(10):
    def display():
        print(f'{n} * 2 = ', n * 2)

    display()


# ++++++++ Returning a function from another function ++++++++
def func(x):
    if x == 1:
        def rv():
            print('X is 1')
    else:
        def rv():
            print('X is NOT 1')

    return rv


print('Printing the functions returned via another function:')

# Getting a function via another function
new_function = func(1)
# Call the function returned
new_function()

new_function_2 = func(2)
new_function_2()

print('Printing the memory address of the new functions:')

# Getting the memony address via the id() built-in function
print('new_function:')
print(id(new_function))
print('new_function_2:')
print(id(new_function_2))


# ++++++++ Displaying the source code of a function ++++++++
print('Printing the source code of functions with inspect.getsource(function_name):')
import inspect
from queue import Queue

print('new_function:')
print(inspect.getsource(new_function))
print('new_function_2:')
print(inspect.getsource(new_function_2))

print('Printing the soruce code of the library queue:')
print(inspect.getsource(Queue))
