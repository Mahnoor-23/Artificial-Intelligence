#while loop
count=0
while(count<3):
    count=count+1
    print("Python")

#Single statement using while loop
#counter=0
#while(counter==0): print("Mahnoor")

#for loop
#example 1
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

#example 2
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

#example 3
print("\nString Iteration")
s="geeks"
for i in s:
    print(i)

#iterating by index
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])

#Print all letters except 'e' and 's'
for letters in 'geeksforgeeks':
    if letters == 'e' or letters == 's':
        continue
    print ('Current Letter:',letters)
    var = 10

#using break 
for letter in 'geeksforgeeks':
    #break the loop as soon it sees 'e' or 's'
    if letter == 'e' or letter == 's':
        break
    print ('Current Letter:',letter)

#defining a function
def my_function():
    print("This is a Function")


my_function()

#passing parameters
def a_function(name):
    #print(name + " Mahnoor")
    print(name)

a_function("Maryam")
a_function("Smavia")
a_function("Musfira")

#default parameter value
def new_function(city = "Gujranwala"): 
    print("I am from "+city)

new_function("Hafizabad")
new_function()
new_function("Lahore")
new_function("Faisalabad")

#passing a list as a parameter
def n_function(food):
    for x in food:
        print(x)

fruits = ["apple", "grapes", "peach"]
n_function(fruits)

#returning values
def mul_function(x):
    return 5*x

print(mul_function(2))
print(mul_function(3))
print(mul_function(4))
print(mul_function(5))

#keyword arguments
def key_function(child1,child2,child3):
    print("The youngest child is "+child3)

key_function(child1 = "Mahnoor", child2 = "Fahad", child3 = "Tehreem")

#creating class
class Myclass:
    x=5

p1 = Myclass() 
print(p1.x)

#_init_() function
#function using class
class Person: 
    def __init__(self,name,age): 
        self.name = name
        self.age = age

p2 = Person("Mahnoor",20)
print(p2.name)
print(p2.age)

#object methods
class Info:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+ self.name)
p1 = Info("Mahnoor",20) 
p1.myfunc()