local_val = "magical unicorns"  # document has a local variable


def square(x):  # document has a function
    return x * x


class User:  # document has a class
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "hello"


print(square(5))  # prints the function output
user = User("Anna")  # creates an instance of User class
print(user.name) #prints Anna
print(user.say_hello()) #hello
print(__name__) #adding htis line is step 1, after namespace, in the modularizing assignment
#line 20 prints _ _main _ _ to the console.
if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
  
