# Start by creating a Store class that has 2 attributes: a name and a list of products. 
# The name must be provided upon creation, but the products list should be empty.
class Store:
    
    def __init__(self, name):

        self.name = name #attribute of the class
        self.product_list = [] #empty #attribute of the class

# Let's also give some methods to our Store class:
# add_product(self, new_product) - takes a product and adds it to the store
    def add_product(self, new_product):

        self.product_list.append(new_product) #.append not += 

# sell_product(self, id) - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
    def sell_product(self, id):

        self.product_list.pop(id)
        print(id)

# inflation(self, percent_increase) - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
# set_clearance(self, category, percent_discount) - 
# updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)    

# Next, create a Product class that has 3 attributes: a name, a price, and a category. 
# All of these should be provided upon creation.
class Product:

    def __init__(self, name, price, category): #name, price, category are parameters.

        self.name = name #attribute
        self.price = price #attribute
        self.category = category #attribute - we can create them, and we can change them

# Product class methods:
# update_price(self, percent_change, is_increased) - updates the product's price. 
# If is_increased is True, the price should increase by the percent_change provided. 
# If False, the price should decrease by the percent_change provided.
    def update_price(self, is_increased, percent_change=0.1):

        if is_increased == True: #double equal for comparison
            amount_increase = self.price*percent_change
            self.price += amount_increase
        else:
            amount_decrease = self.price*percent_change
            self.price -= amount_decrease

# print_info(self) - print the name of the product, its category, and its price.
    def print_info(self):

        print(f"Name: {self.name}, Price: {self.price}, Category: {self.category}")

#create an instance of the Store class
Target = Store("target")
print(Target)
#create instances for the Product class
Belt1 = Product("Burberry",460,"Luxory")
print(Belt1)
Belt2 = Product("Patagonia", 100, "Outdoors")
print(Belt2)
Belt3 = Product("Balenciaga", 500, "Luxory")
print(Belt3)

#add instances to the store instance
Target.add_product(Belt3) #Target is the name of the Store
Target.add_product(Belt2)
Target.add_product(Belt1)

Belt1.print_info()
Belt2.print_info()
Belt3.print_info()

Belt1.update_price(True)
Belt1.print_info()