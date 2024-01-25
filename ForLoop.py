    # Print Hello multiple times 
for x in range(3):
    print("Hello")

    # Print 1st 10 natural numbers
for i in range(1,9+1) :
    print(i)

    # Print sum of n natural numbers
sum = 0
n = int(input("Enter n : "))
for i in range(1,n+1) :
    sum = sum+i
print("The Sum of first n Natural numbers is : ",sum)

    # Print Product of n natural numbers
p = 1
for i in range(1,n+1) :
    p *= i
print("The Product of first n Natural numbers is : ",p)

    # Print 10 numbers in decreasing order.
for i in range(10, 0, -1) :
    print(i)

    # Iteration using 3 parameters in range
for i in range(1,12,3) :
    print(i)

    # Iteration of String
str = "Fawzaan"
for i in str:
    print(i)

    # Iteration of a List
my_list = ["I","am","Coder"]
for i in my_list:
    print(i)