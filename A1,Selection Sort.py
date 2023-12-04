def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp

n=int(input("Enter the number of element in the array:"))
arr=[]
for i in range(n):
    element=int(input(f"Enter element{i+1}:"))
    arr.append(element)
print("Orginal Array:",arr)
selection_sort(arr)
print("Sorted array:",arr)


