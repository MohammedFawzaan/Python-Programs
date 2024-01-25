a = int(input("Enter a "))
match a :
    case 0 :
        print("x is zero")
    case a if a%2==0:
        print(a,"is even")
    case a if a%2==1:
        print(a,"is odd")
    # default case 
    case _:
        print(a)