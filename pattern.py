def pypart(n):
    # number of spaces
    k = 2 * n - 2

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

            # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars  if you want number in place of star(*) then replace print(i," " , end="")
            print("* ", end="")

            # ending line after each row
        print("\r")

def printNumber(n):
    k= 2*n -2  #k is number is spaces

    for i in range(0,n): # outer loop to handle of number of row

        for j in range(0,k): # this looop to handle number of spaces & this will change according to requirment
            print(end = " ")
        k = k-1   # decrement k after each loop

        for j in range(0,i + 1):
            print(j ," ",end="")
        print("\r") # for end each row

def pascal(n):
    k = 2 * n -2
    for line in range(1, n+1):
        for j in range(0,k):
            print(end = " ")
        k=k-1
        # Every line has number of
        # integers equal to line
        # number
        C = 1;  # used to represent C(line, i)
        for i in range(1, line + 1):
            # print(binomialCoeff(line, i),
            #       " ", end="")
            print(C, end=" ");
            C = int(C * (line - i) / i);
        print("\r")

        # See https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/

    # for details of this function
def binomialCoeff(n, k):
        res = 1
        if (k > n - k):
            k = n - k
        for i in range(0, k):
            res = res * (n - i)
            res = res // (i + 1)

        return res

n = int(input("enter any number"))
pypart(n)
printNumber(n)
pascal(n)