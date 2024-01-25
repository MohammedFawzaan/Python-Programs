# largest of three numbers
a = int(input("Enter a  : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
if a>=b and a>=c :
    print(a, " is largest")
elif b>=a and b>=c :
    print(b," is largest")
else :
    print(c, " is largest")

# Even Odd Program
if a%2==0 :
    print(a, "even")
else :
    print(a, "odd")