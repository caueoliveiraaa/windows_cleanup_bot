# Creating a metaclass (type is necessary as a parameter)
class Meta(type):
    # Dunger method the executes before the init method
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        dict_attrs = {}
        for name, value in attrs.items():
            if name.startswith('__'):
                dict_attrs[name] = value
            else:
                dict_attrs[name.upper()] = value

        print(dict_attrs)
        return type(class_name, bases, dict_attrs)
    
class Dog(metaclass=Meta):
    x = 5
    y = 5

    def greet(self):
        print('Hello humans.')