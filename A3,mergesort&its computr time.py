import time
import random
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        B = arr[:mid]
        C = arr[mid:]

        merge_sort(B)
        merge_sort(C)

        i = j = k = 0

        while i < len(B) and j < len(C):
            if B[i] <= C[j]:
                arr[k] = B[i]
                i += 1
            else:
                arr[k] = C[j]
                j += 1
            k += 1

        while i < len(B):
            arr[k] = B[i]
            i += 1
            k += 1

        while j < len(C):
            arr[k] = C[j]
            j += 1
            k += 1


n=int(input("Enter the number of elements(more than 5000): "))
arr=[random.randint(1,100000) for _ in range(n)]
start_time = time.time()
merge_sort(arr)

end_time = time.time()
print("Time taken to sort:", end_time - start_time, "seconds")


