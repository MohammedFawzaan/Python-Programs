# To print Length of a String
name = "Mohammed Fawzaan"
len1 = len(name)
print(len1)

# String Slicing
a = "Fruit" # length = 5, index from 0 to 4
a1 = a[0:5] # include 0 index & exclude 5 index
a2 = a[:5]  # starts from 0 and ends at 4th index
a3 = a[3:]  # starts from 3rd index and ends at last index
print(a1)
print(a2)
print(a3)
print(a[2:3])
print(a[2:])

# Negative String Slicing
b = "Mango" # length = 5, index from 0 to 4
b1 = b[0:-3] # starts from 0 index and ends at len(b)-3 excluded
print(b1)
b2 = b[-2:] # starts from len(b)-2 included and ends at last index
print(b2)
b3 = b[-4:-1]
print(b3)

nm = "Harry"
print(nm[-4:-2])

app = "Instagram"
print(app[6]) # Print data at specific index

s = "Python"
print(s[:6])
print(s[0:4])
print(s[3:5])
print(s[-4:])