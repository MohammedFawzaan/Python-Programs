    # Print 1st 5 numbers
count = 0
while(count<=5):
    print(count)
    count += 1

    # Print 5 numbers in reverse order
count = 5
while(count>=0):
    print(count)
    count -= 1
else :
    print("I'm inside else")
    # Print sum of numbers until the user enter zero
sum = 0
while(True):
    n = int(input("N = "))
    if(n==0):
        break
    sum += n
print("Sum of numbers you entered is : ",sum)