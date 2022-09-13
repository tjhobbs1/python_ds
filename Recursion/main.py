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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   recursiveMethod(5)


