######### Merge sort ##########

def merger_two_sorted_list(List_1,List_2):
    len_1=len(List_1)
    len_2=len(List_2)
    sorted_list=[]
    pointer_1=0
    pointer_2=0
    while pointer_1<len_1 and pointer_2<len_2:
        if List_1[pointer_1]<List_2[pointer_2]:
            sorted_list.append(List_1[pointer_1])
            pointer_1+=1
        else:
            sorted_list.append(List_2[pointer_2])
            pointer_2+=1
    while pointer_1<len_1:
        sorted_list.append(List_1[pointer_1])
        pointer_1+=1
    while pointer_2<len_2:
        sorted_list.append(List_2[pointer_2])
        pointer_2+=1
    return sorted_list

def splitter_and_sorter(Array):
    if len(Array)==0 or len(Array)==1:
        return Array
    else:
        middle=len(Array)//2
        return merger_two_sorted_list(splitter_and_sorter(Array[:middle]),splitter_and_sorter(Array[middle:]))

z = splitter_and_sorter([7,8,3,5,4,2,8,9])
print(z)