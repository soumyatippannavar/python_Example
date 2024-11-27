from Inheritance import A

class computer(A):
    def __init__(self):
        self.age=10
        self.name='ramya'

    def compare(self,c2):
        if c1.age==c2.age:
            print("they are same")
        else:
            print("they are diff")

c1=computer()
c2=computer()
print(c1.age)
c1.age=20
print(c1.age)

if c1.compare(c2):
    print("true")

else:
    print("false")

