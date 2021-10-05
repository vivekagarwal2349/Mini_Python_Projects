# Our Input Array
arr = [3,2,4,1]

def Cyclic_sort(arr):
    """
    This function will check if the element at i is at the correct index
    or not. If it is not at the correct index then it will swap places and if 
    it is then we will increment the value of i by 1.
    """
    i = 0

    while i < len(arr):
        correct_index = arr[i] - 1

        if arr[i] != arr[correct_index]:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]

        else:
            i += 1
    return arr
print(Cyclic_sort(arr))
