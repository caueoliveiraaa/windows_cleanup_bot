# NOTE: Classes in Python are objects, meaning with can pass them as paramaters,
# we can assign them to variables, we can modify them, etc. 


class Test:
    pass

class func():
    pass

print(Test)  # <class '__main__.Test'> 
print(type(Test()))  # <class '__main__.Test'>
print(func)  # <class '__main__.func'>
print(type(Test))  # <class 'type'>   -   (metaclass)


# NOTE: Creating classes dynamically.
# 'Test': This is the name of the new class that you’re creating.
# (): This is a tuple containing the base classes that your new class will inherit from. 
#      In this case, it’s empty, so your class doesn’t inherit from any other classes.
# {}: This is a dictionary containing attributes and methods for your new class.
#      Since it’s empty, your class doesn’t have any predefined attributes or methods.

Test = type('Test', (), {})
print(Test)  # <class '__main__.Test'>  

# NOTE: Adding a method to the class.

def hello_world(self):
    print('Hello world!')

Test = type('Test', (), {'hello_world': hello_world})
test = Test()
test.hello_world()