def binary_search(elem,arr,left,right):
    if left==right:
        return False
    else:
        mid=(left+right)//2
        if arr[mid]==elem:
            return True
        elif elem<arr[mid]:
            right=mid-1
            return binary_search(elem,arr,left,right)
        else:
            left=mid+1
            return binary_search(elem,arr,left,right)
elem=int(input())
arr = [1,2,3,4,5,6,7,7,8]
print(binary_search(elem,arr,0,len(arr)))