def sort(lis,n):


    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
def sorted_Merge(a, b, res, n, m):
    # Sorting a[] and b[]
    sort(a,n)
    sort(b,m)

    # Merge two sorted arrays into res[]
    i, j, k = 0, 0, 0
    while (i < n and j < m):
        if (a[i] <= b[j]):
            res[k] = a[i]
            i += 1
            k += 1
        else:
            res[k] = b[j]
            j += 1
            k += 1

    while (i < n):  # Merging remaining
        # elements of a[] (if any)
        res[k] = a[i]
        i += 1
        k += 1

    while (j < m):  # Merging remaining
        # elements of b[] (if any)
        res[k] = b[j]
        j += 1
        k += 1


# Driver code
a = [10, 5, 15]
b = [20, 3, 2, 12]
n = len(a)
m = len(b)

# Final merge list intially contain 0
res = [0 for i in range(n + m)]
sorted_Merge(a, b, res, n, m)
print("Merge List:{}".format(res))