# *** Docs: https://docs.python.org/3/reference/datamodel.html ***

# Adding a list to another one
list_1 = [1, 2, 3]
list_2 = [4, 5]
list_3 = list_1 + list_2
print(f'Printing the list {list_1} and the list {list_2} after joining them both:')
print(list_3)



# ****************** Dunger / Magic methods *********************
class Person():
    def __init__(self, name):
        self.name = name

    # Dunger method repr (string representation of the object)
    def __repr__(self):
        return f"Person({self.name})"
    
    # Dunger method mul (what happens when objects of this class are multiplied)
    def __mul__(self, x: int) -> None:
        if type(x) is not int:
            raise ValueError(f'Value {x} is not int.')

        self.name = self.name + x

    # Dunger method call (executes code when object is called)
    def __call__(self, arg: int) -> None:
        if type(arg) is not int:
            raise ValueError(f'Value {arg} is not int.')
        
        print(f'Object involked with argument: int = {arg}.')

    # Dunger method len (represents the size of the object)
    def __len__(self) -> str:
        return len(str(self.name))

person_object = Person("Smith")
person_object(7)
print(len(person_object))
print(person_object.name)



# +++++++++ Working with Queue +++++++++
from queue import Queue
import inspect

# The queue object does not have a repr dunger method
q = Queue()
print(q) # Memory address

# Displaying the source code of the class Queue
print(inspect.getsource(Queue))

# Inheriting the Queue class
class MyQueue(Queue):
    # Asigning a repr method to the class
    def __repr__(self) -> None:
        return f'Queue({self._qsize()})'
    
    # Giving the class the ability to sum
    def __add__(self, item) -> None:
        self.put(item)
    
qu = MyQueue()
print(qu)
qu + 5
print(qu)
qu + '5'
print(qu)