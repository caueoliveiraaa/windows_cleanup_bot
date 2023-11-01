# NOTE - creating a metaclasses:

# type is necessary as a parameter
class Meta(type):
    # Dunger method the executes before the init method
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        # Changing attributes of the class to uppercase
        dict_attrs = {}
        for name, value in attrs.items():
            if name.startswith('__'):
                dict_attrs[name] = value
            else:
                dict_attrs[name.upper()] = value

        print(dict_attrs)
        return type(class_name, bases, dict_attrs)
    

class Bot(metaclass=Meta): 
    x = 5
    y = 15
    s = '459687'

    def greet(self):
        print('Hello humans.')


#   *** LOOK UP THE DOCS ON IT ***

if __name__ == '__main__':
    bot = Bot()
    bot.GREET()
    print(bot.S)
    print(bot.X)
    print(bot.Y)