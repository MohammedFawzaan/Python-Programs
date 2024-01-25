class Student:
    def __init__(self,value):
        self._value = value

    # Getter function used to access the value and return the value of specific property, Takes no argument
    @property #function to be used for getting an attribute value
    def getter(self): 
        return self._value
    
    def show(self): # To print the Getter value of a function.
        print(f"Value : {self._value}")

    # Setter function used to set the value to new value and take atleast one argument
    @getter.setter # '@property_name'.setter
    def setter(self, new_value):
        self._value = 10*new_value # Setting new value to var value
        
    
s1 = Student(67)
s1.getter
s1.show()

s1.setter = 100
print("New_Value : ",s1.setter)