# def add(*args):  # *args takes any amount of arguments
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(5, 2, 6, 9))

def calculate(n, **kwargs):  # **kwargs(key word arguments allows you to create dictionaries having key:value pairs
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

    # print(kwargs["add"])

calculate(2, add=4, multiply=7)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.doors = kw.get("doors")

my_car = Car(make="Toyota", model="Tacoma", color="Plutonium Grey", doors=4)

print(my_car.color)