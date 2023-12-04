def max_min_divide_conquer(arr, low, high):
    class Pair:
        def _init_(self):
            self.max = 0
            self.min = 0
    result = Pair()
    if low == high:
        result.max = arr[low]
        result.min = arr[low]
        return result
    if high == low + 1:
        if arr[low] < arr[high]:
            result.min = arr[low]
            result.max = arr[high]
        else:
            result.min = arr[high]
            result.max = arr[low]
        return result
    mid = (low + high) // 2
    left = max_min_divide_conquer(arr, low, mid)
    right = max_min_divide_conquer(arr, mid + 1, high)
    result.max = max(left.max, right.max)
    result.min = min(left.min, right.min)
    return result
n=int(input("Enter the number of element in the array:"))
arr=[]
for i in range(n):
    element=int(input(f"Enter element{i+1}:"))
    arr.append(element)
result = max_min_divide_conquer(arr, 0, len(arr) - 1)
print("Maximum element is:", result.max)
print("Minimum element is:", result.min)