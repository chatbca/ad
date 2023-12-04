import random
import time
def partion(arr,left,right):
    pivot=arr[left]
    i=left
    j=right+1
    while True:
        i+=1
        while i<= right and arr[i]<= pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i>=j:
          break
        arr[i],arr[j]=arr[j],arr[i]
    arr[left],arr[j]=arr[j],arr[left]
    return j

def quicksort(arr,left,right):
    if left<right:
        pivot_index=partion(arr,left,right)
        quicksort(arr,left,pivot_index-1)
        quicksort(arr,pivot_index+1,right)


n = int(input("Enter the number of elements(more than 5000): "))
arr=[random.randint(1,100000) for _ in range(n)]
start_time = time.time()
quicksort(arr,0,len(arr)-1)
print(arr)
end_time = time.time()
print("Time taken to sort:", end_time - start_time, "seconds")
