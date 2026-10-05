#Task 8
#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i, end = "")


#Task 9
#Write a Pyhton program to get a Fibonacci series b/w 0 to 50.
a = 0
b = 1
while a <= 50:
    print(a, end = " ")
    c = a + b
    a = b
    b = c


#Write a Python program which iterates from 1 to 50.
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#Task 10
#Write a program which takes two digits m(row) and n(column) as input and generates a two-dimensional array.
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
arr = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(i * j)
    arr.append(row)
print(arr)


#Task 11
#Write a Python program that accepts a sequence of lines as input and prints the lines as output.
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line.lower())
for line in lines:
    print(line)


#Task 12
#Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.
numbers = input("Enter binary numbers: ").split(",")
result = []
for num in numbers:
    if int(num, 2) % 5 == 0:
        result.append(num)
print(",".join(result))


#Task 13
#Write a Python program that accepts a string and calculate the number of digitsand letters.
string = input("Enter a string: ")
letters = 0
digits = 0
for ch in string:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Number of Letters in string are: ",letters)
print("Number of Digits in string are: ",digits)

#Task 14
#Write a Python program to check the validity of password input by users.
password=input("Enter Password : ")
lower=False
upper=False
digit=False
special=False
for character in password:

    if character.islower():
        lower = True

    elif character.isupper():
        upper = True    

    elif character.isdigit():
        digit = True

    elif character in "$#@":
        special = True
    
if(6 <= len(password) <=16 and lower and
    upper and digit and special):
        print("Valid password ")    
else:
        print("Invalid password")