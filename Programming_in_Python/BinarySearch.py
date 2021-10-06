def binarySearch(arr, target):                #function for searching a target using binary search algorithm
    start = 0
    end = len(arr) - 1
    middle = 0

    while start <= end:
        middle = start + (end - start) // 2

        if arr[middle] > target:              #if target is smaller than middle element, there's a chance that the target may lie to middle element's left
            end = middle - 1                  #Therefore, we update end accordingly
        elif target < arr[middle]:            #if target is larger than middle element, there's a chance that the target may lie to middle element's right side
            start = middle + 1                #Therefore, we update start accordingly
        else:                                 
            return middle                     #return middle(index) if target == arr[middle]

    return -1


arr = [1, 2, 3, 4, 5, 6]
target = 2

result = binarySearch(arr, target)

if result != -1:
    print(result)
else:
    print("Invalid")
