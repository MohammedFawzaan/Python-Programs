def name(A, B, C):          # Example for return stmt
    return ("Hello,"+A+" "+B+" "+C)
print(name("a","b","c"))

def sum(a=10,b=20):         # Default Arguments
    return a+b
print(sum())

def product(a,b,c):         # Keyword Arguments
    return a*b*c
print(product(c=1,a=8,b=4))