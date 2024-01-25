class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def function(self):
        print("Name : ", self._name,",age : ",self._age)
obj1 = Student("Fawzaan",19)
obj2 = Student("Abusufyan",20)
obj3 = Student("Towhid",19)

obj1.function()
obj2.function()
obj3.function()