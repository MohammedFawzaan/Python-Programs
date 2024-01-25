# Single Level Inheritance.
class Parent():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def property(self):
        car = "10,000,000"
        print(f"Our Car price = {car}")
    def profession(self):
        print("My profession is Teaching")
class Child(Parent):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def iamprogrammer(self):
        print(f"{self.name} is a Programmer")
class Child2(Parent):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def iamGamer(self):
        print(f"{self.name} is a Gamer")
p = Parent("Mamma",40)
print("Name:",p.name)
print("age:",p.age)
p.profession()
p.property()
print("\n")
c1 = Child("Fawzaan",19)
print("Name:",c1.name)
print("age:",c1.age)
c1.property()
c1.iamprogrammer()
print("\n")
c2 = Child2("Shahaan",10)
print("Name:",c2.name)
print("age:",c2.age)
c2.property()
c2.iamGamer()