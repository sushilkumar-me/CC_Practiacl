a = [4,5,2,8,10]
tracker = 1
for i in range(len(a)):
    k = 0
    for j in range(i,len(a)-1):
        if a[i] < a[j+1]:
            a[i] = a[j+1]
            k = 1
            break
    if k == 0: 
        a[i] = -1
    

print(a)
