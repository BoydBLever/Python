num1 = 42 
# variable declaration, data type: primitive: numbers
num2 = 2.3 
# variable declaration, data type: float
boolean = True 
# variable declaration, data type: Boolean
string = 'Hello World' 
# variable declaration, data type: string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# initialize a data type, composite list.
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# initialize composite data type, dictionary
fruit = ('blueberry', 'strawberry', 'banana')
# initialize composite data type, tuples
print(type(fruit))
# type check
print(pizza_toppings[1])
# access value in list
pizza_toppings.append('Mushrooms')
# add value in list
print(person['name'])
# access value in dictionary
person['name'] = 'George'
# change value in dictionary
person['eye_color'] = 'blue'
# add value in dictionary
print(fruit[2])
# access value in tuple
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# conditional if else statement
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# conditional if elif else statement
for x in range(5):
    print(x)
# for loop start 0 stop 4
for x in range(2,5):
    print(x)
# for loop start 2 stop 4
for x in range(2,10,3):
    print(x)
# for loop start 2 stop 9, step 3
x = 0
while(x < 5):
    print(x)
    x += 1
# while loop start 0, stop 4, increment by 1
pizza_toppings.pop()
# removes the last value in pizza toppings list
pizza_toppings.pop(1)
# not possible
print(person)
# accesses the dictionary value
person.pop('eye_color')
# not possible
print(person)
# not possible
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# for loop with continue and break
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
# function and for loop
print_hello_ten_times()
# function

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
# function and foor loop

print_hello_x_times(4)
# function prints hello x times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
# function prints hello x times
print_hello_x_or_ten_times()
# function
print_hello_x_or_ten_times(4)
# function

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)