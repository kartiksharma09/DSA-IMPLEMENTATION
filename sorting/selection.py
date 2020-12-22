############ SELECTION SORT #################

a = [1,3,2,5,4,7,6,9,8]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

print(a)