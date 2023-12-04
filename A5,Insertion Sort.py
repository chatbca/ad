def insertion_sort(arr):
    n=len(arr)
    if n<=1:
        return
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key

n=int(input("Enter the number of element in the array:"))
arr=[]
for i in range(n):
    element=int(input(f"Enter element{i+1}:"))
    arr.append(element)
print("Orginal Array:",arr)
insertion_sort(arr)
print("Sorted array:",arr)