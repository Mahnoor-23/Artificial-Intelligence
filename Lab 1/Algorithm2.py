L1 = [1,2,3,4]
L2 = [6,7,8,9]

t = int(input("Enter a number "))
for i in range(len(L1)):
    if L1[i] == t:
        print("True")
        break

else:
    for i in range(len(L2)):
        if L2[i] == t:
            print('True')
            break
        else:
            print('false')