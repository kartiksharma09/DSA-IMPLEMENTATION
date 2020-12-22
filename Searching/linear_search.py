arr = [2,4,3,5,67,8,9809,9]
val = int(input())
for index,value in enumerate(arr):
    if value == val:
        print("your value is at index :",index)
        break