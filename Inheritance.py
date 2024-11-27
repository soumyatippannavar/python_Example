class A:
    digit=10
    def __init__(self,name):
        print("from A contsructor of A")
        self.name=name
        print(self.name)

    def feature1(self):
        print("feature 1------ ")
        print("after:" + self.name)

    def feature2(self):
        print("feature 2------ ")
    def feature3(self):
        print("feature 3------ ")


class B:

    def feature3(self):
        print("feature 3------ ")

    def feature4(self):
        print("feature 4------ ")


class C(A,B):
    def __init__(self):
        #super().__init__(name)
        self.nam="r"
        print("from constructor of C")

    def feature5(self):
        #self.name="abc"
        super().__init__("name")
        self.name="ramya"
        print("feature 5------ ",self.name)


    def feature1(self):
        print("inheritted overriding method:", self.digit)

#b=A("RAMYA")
#b.feature1()
c=C()
#c=C()
#c.feature3()
c.feature5()
#c.feature1()
print(c.name)