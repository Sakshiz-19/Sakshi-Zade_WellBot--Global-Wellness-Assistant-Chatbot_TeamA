# Program to demonstrate enumerate()

fruits = ["apple", "banana", "cherry"]

print("Using enumerate with default start:")
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("\nUsing enumerate with custom start:")
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


    # Program to demonstrate isinstance()

x = 10
y = "Hello"
z = [1, 2, 3]

print("x is int:", isinstance(x, int))        # True
print("y is str:", isinstance(y, str))        # True
print("z is list:", isinstance(z, list))      # True
print("y is int:", isinstance(y, int))        # False

# Checking against multiple types
print("x is int or float:", isinstance(x, (int, float)))  # True


import gc

class Demo:
    def __del__(self):
        print("Object destroyed")

# Disable automatic garbage collection
gc.disable()
print("Garbage collection disabled")

obj = Demo()
del obj  # Object is not immediately destroyed because GC is off

print("Manually running garbage collector...")
gc.collect()  # Forces garbage collection
gc.enable()
print("Garbage collection enabled again")
