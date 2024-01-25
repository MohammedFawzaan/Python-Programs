   # Default Arguments

def sum(a, b, c=2, d=1):
    return a+b+c+d
sum = sum(1,9)
print(sum)

def average(a,b=9):
    return (a+b)/2
average = average(10)
print(average)

def diff(a=100,b=1):
    if(a>b):
        return a-b
    else:
        return b-a
print(diff())

    # Keyword Arguments

def product(a, b, c, d):
    return a*b*c*d
product = product(5 ,c=1, d=3, b=2)
print(product)

    # Required Arguments

def name(fname, mname, lname):
    print("Hello,", fname, mname, ":", lname)
name("Peter", "Quill", "StarLord")

    # Variable Length Arguments

# --> Arbitary Arguments
def name(*tuple):
    print(type(tuple))
    print("Hello,", tuple[0], tuple[1], tuple[2])
name("H","O","P")
# Take parameter in form of tuple if we put * before parameter name
def sum(*tuple):
    print(type(tuple))
    sum = 0
    for i in tuple:
        sum = sum + i
    print(sum)
sum(1,2,3,4,5,6,7,8,9,10)

# --> Keyword Arbitary Arguments
# Take parameter in form of dictionary if we put ** before parameter name
def name(**dict):
    print(type(dict))
    print(dict["n1"], dict["n2"], dict['n3'])
name(n1=1, n2=2, n3=4) # here n1 n2 n3 are key values which are used to access a dict (ie index) and 1 2 4 are variables