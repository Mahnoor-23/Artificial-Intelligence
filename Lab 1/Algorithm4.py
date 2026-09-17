L1 = [1,2,3,4,5,3,6]
for i in range(len(L1)):
    for j in range(i+1 ,len(L1)):
        if L1[i] == L1[j]:
            print("Duplicate number Found")
            break
    else:
        continue
    break    
else:
    print("Duplicate number not found")    