# INPUT ARRAY -
arr = [5,2,8,1,6]

def Bubble_Sort(arr):
    """
    This functions loops through the array with an upper range of outer loop
    and it checks two elements at a time if the previous element is greater 
    than the one next to it they swap their places.
    """

    for i in range(0, len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr

print(Bubble_Sort(arr))
