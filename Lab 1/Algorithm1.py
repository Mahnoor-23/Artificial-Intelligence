list= [1,2,3,4,5,6]   
t = int(input("Enter a number: "))

for i in range(len(list)):
    if list[i] == t:
        print('true')
        break
else:
    print('false')

