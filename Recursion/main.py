"""
Recursion Example
"""

def recursiveMethod(n):
    #Base Case
    if n < 1:
        print("N is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

def powerOfTwo(n):
    #Base Case
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        x = power * 2
        print(x)
        return x

def powerOfTwoIterative(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i += 1
    return power


if __name__ == '__main__':
   #recursiveMethod(5)

   print(powerOfTwo(5))


