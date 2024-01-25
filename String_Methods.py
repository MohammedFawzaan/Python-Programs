# Strings are immutable 
str1 = "AbCDef"
print(len(str1))
print(str1.upper())
print(str1.lower())

str2 = "Hello !!"
print(str2.rstrip("!"))

str3 = " Silver Spoon "
print(str3.replace("00","M"))
print(str3.strip().replace("Sp","M"))

str4 = "Welcome to python fAWZAAN"
capstr4 = str4.capitalize()
print(capstr4)
print(str4.center(51,"_"))
titleCap = str4.title()
print(titleCap)
print(str4.swapcase())

str5 = "Harry Harry harry Fawzaan"
print(str5.count("a"))
print(str5.count("Harry"))

str6 = "Python Programming"
print(str6.endswith("ming"))
print(str6.endswith("o"))
print(str6.startswith("Python"))

str6 = "Ok"
print(str6.endswith("k",0,2))

str7 = "My name is Fawzaan"
print(str7.find("F"))
print(str7.index("F"))

str8 = "Welcometopython"
print(str8.isalnum())
str8 = "Welcom!@#$%!"
print(str8.isalnum())
str8 = "WELCome"
print(str8.isalpha())
str8 = "324"
print(str8.isalpha())