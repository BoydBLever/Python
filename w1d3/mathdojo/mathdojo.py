class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for num in nums:
            self.result += num
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for num in nums:
            self.result -= num
        return self
# create an instance:
md = MathDojo() #creating an instance of an object. md is stored as an instance of mathdojo. () initializes the object.
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result #using the methods from the class, MathDojo
print(x)	# should print 5
# run each of the methods a few more times and check the result!