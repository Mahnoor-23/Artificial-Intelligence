#simple print statemant
print("Hello World")
#writing comments
x=1
# the value of x is 1
if(x>0):
    print("Comment are written in the task!")

#getting input from user
t = input("Enter the value: ")   
print(t)

#multiple statement
print("Statement1")
print("Statement2")

#we can write multiple statements as:
print("Statement1") ; print("Statement2")

#indentation
y=1
#if y>0:
#print("This statement has no indentation")
#print("This statement has no indentation")

#single space indentation
z=1
if z>0:
 print("This statement has indentation")
 print("This statement has indentation")

#single tab indentation
u=1
if u>0:
    print("This statement has indentation")
    print("This statement has indentation")

#different datatypes 
a = 1234
print(type(a))

b = (-1234)
print(type(b))

c = 0
print(type(c))

d = 1.234
print(type(d))

e = (-1.234)
print(type(e))

f = .234
print(type(f))

g = 1.23e-10
print(type(g))

h = 1E234
print(type(h))

#real and imaginary numbers
i = complex(1,3)
print(type(i))
print(i)

k = 2+3j
print(type(k))
print(k)

l = 2+3J
print(type(l))
print(l)

#bool expression
m = True
print(type(m))

n = False
print(type(n))

#strings
str1 = "String1"
print(str1)

str2 = 'String2'
print(str2)

#str3 = "String3'
#print(str3) 
#error bcz string start with double quote and end with single quote

#str4 = 'String4" 
#print(str4) 
#error bcz string start with single quote and end with double quote

str5 = "Day's" 
print(str5)

str6 = 'Day"s'
print(str6)

#escape sequence
print("This is a blackslash (\\) mark.")
print("This is a  tab \t  key   ")
print("These are \'single quote\'")
print("These are \"double quote \"")
print("This is a Newline \n Newline")

#accessing string element using indexes
string1 = "PYTHON TUTORIAL"
print(string1[0])
print(string1[-15])
print(string1[14])
print(string1[-1])
print(string1[4])
print(string1[-11])
#print(string1[16]) 
#error bcz it is out of index range 

#creating list 
l1 = [5, 12, 13, 14]   #list have integer values
print(l1)

l2 =['red' , 'blue' , 'black' , 'green']
print(l2)
#print(l2[2]) 

l3 = ['red ' ,2, 4, 7.5 , 'pink'] #list contains integer float and string values
print(l3)

l4 = []
print(l4)

#accessing element of list 
colors =['red' , 'blue' , 'black' , 'green', 'pink' , 'grey']
print(colors)
print(colors[0]) 
print(colors[0] , colors[3]) 
print(colors[-1]) 
print(colors[4]) 
print(colors[5]) 
print(colors[-2]) 

#list slicing
print(colors[0:2])
print(colors[1:2])
print(colors[1:-2])
print(colors[2:])
print(colors[:3])
print(colors[:])
