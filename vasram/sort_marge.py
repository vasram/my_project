def sort(lis,n):


    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                swapped = True
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




a = []
size = int(input("Enter The first size : "))
for element in range(0, size):
    print("Enter the {} Element".format(element + 1), end = " " )
    a.append(int(input()))

b = []
size = int(input("Enter The first size : "))
for element in range(0, size):
    print("Enter the {} Element".format(element + 1), end = " " )
    b.append(int(input()))

# Final merge list intially contain 0
res = [0 for i in range(len(a) + len(b))]
sorted_Merge(a, b, res, len(a), len(b))
print("Merge List:{}".format(res))