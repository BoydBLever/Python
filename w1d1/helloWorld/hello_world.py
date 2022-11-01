# I used f strings for everything
# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Boyd"
print("Hello", f"{name}!")  # with a comma
print("Hello" + " " + f"{name}!")  # with a +
# 3. print "Hello 42!" with the number in a variable
num = 2
print("Hello", f"{num}!")  # with a comma
# with a +	-- this one should give us an error!
print("Hello" + " " + f"{num}!")
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "coffee"
fave_food2 = "sparkling water"
print("I love to drink " + f"{fave_food1}" + " and " + f"{fave_food2}.")
