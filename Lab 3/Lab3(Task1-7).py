#Task 1
#Write a Python program to find those numbers which are divisible by 7 and multiple of 5 b/w 1500 and 2700.
for i in range(1500, 2700):
    if i % 7 == 0 and i % 5 == 0:
        print(i)


#Task 2
#Write a Python program to convert temperatures to and fromCelsius,Fahrenheit.
c = float(input("Enter temperature in Celsius: "))
f = (c * 9 / 5) + 32
print(c, "C in Fahrenheit is ", int(f))

f = float(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5 / 9
print(f, "F in Celsius is ", int(c))


#Task 3
#Write a Python program to guess a number b/w 1 to 9.
import random
num = random.randint(1, 9)
while True:
    guess = (int(input("Guess a number b/w 1 and 9: ")))
    if guess == num:
        print("Well Guessed!")
        break
    else:
        print("Wrong Guess. Try again!")


#Task 4
#Write a Python program to construct the following pattern, using a nested for loop.
n = 5
#For upper half
for i in range(1, n+1):
    for j in range(i):
        print("*",end = "")
    print()

#For lower half
for i in range(n-1, 0, -1):
    for j in range(i):
        print("* ",end = "")
    print()


#Task 5
#Write a Python program that accepts a word from the user and reverse it.
word = input("Enter a word: ")
reverse = word [::-1]
print("Reverse word is:", reverse)


#Task 6
#Write a Python program to count the number of even and odd numbers from a series of numbers.
#Sample numbers : numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
Numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even = 0
odd = 0
for num in Numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Number of evens: ",even)
print("Number of odds: ",odd)


#Task 7
#Write a Python program that prints each items and its corresponding type from a following list.
List = [1234, 43.4, 2+3j, True, 'Mahnoor', (0, -1), [5, 12], {"Class":'AI', "Section":'BSIT'}]
for item in List:
    print(item ,type(item))