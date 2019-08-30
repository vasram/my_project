# Python3 program for find maximum and minimum element
#  from any unsorted array in time complexity O(n)
def MaxMin(arr, n):
    # Initialize maximum  and minimum element
    max, min = arr[0], arr[0]

    # Traverse array elements from second
    # and compare every element with
    # current max and min and replace if need
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return max, min



arr = []
size = int(input("Enter The Array size : "))
for element in range(0, size):
    print("Enter the {} Element".format(element + 1), end = " " )
    arr.append(int(input()))

max, min = MaxMin(arr, size)
print ("Input : {}".format(arr))
print("Output :")
print("       - Largest number in array is : {}  ".format(max))
print("       - Smallest number in array is : {}  ".format(min))
