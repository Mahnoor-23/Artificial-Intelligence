L1 = [1, 2, 3, 4]
L2 = [5, 6, 2, 8]

t = int(input("Enter a number: "))
for i in range(len(L1)):
    for j in range(len(L2)):
        if L1[i] == L2[j]:
            print('Found')
            break
    else:
        continue
    break    

else:
    print('Not Found')    

    
