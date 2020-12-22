############### INSERTION SORT ##############

unsorted_list = [1,7,3,8,4,6,2,5]
for i in range(len(unsorted_list)):
    for j in range(1,len(unsorted_list)):
        if unsorted_list[j]<unsorted_list[j-1]:
            unsorted_list[j-1],unsorted_list[j]=unsorted_list[j],unsorted_list[j-1]
print(unsorted_list)