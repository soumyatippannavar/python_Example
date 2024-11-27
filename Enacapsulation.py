class Base:
    def __init__(self):
        self._a = 2   # Protected member
        self.__b = 3  #private member

    def ptot(self):
        print(self._a)
        self.__b=4
        print(self.__b)


# Creating a derived class
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ",self._a)
        #print("Calling private member of base class: ",self.__b)
        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",self._a)

    def b(self):
        print(self._a)


obj1 = Derived()
obj1.b()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)
obj2.ptot()

