# Part 1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1. Change the value 10 in x to 15.
x[1][0] = 15
#2. Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = ['Bryant']
#3. In the sports directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]=['Andres']
#4. Change the value 20 in z to 40
z[0]['y'] = 30

#-------------------------------------------------------------
# Part 2 Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for dictionary in students:
        for key in dictionary:
            print(f"{key}-{dictionary[key]}")

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

iterateDictionary(students)