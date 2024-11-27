class methods:

    school='abcds'

    def __init__(self, name, add):
        self.name1 = name
        self.add1 = add

    def display(self):
        return self.name1+self.add1

    def get_name(self):
        return self.name1

    def set_name(self,value):
        m1.add1 = value
        #m1.information()
        return m1.add1
    @classmethod
    def info(cls):
        print(cls.school)

    @staticmethod
    def information():
        a=10
        print("static method")
        print(a)

m1=methods("ramya","tippannavar")
print(m1.display())
print(m1.get_name())
methods.info()
methods.information()
print(m1.get_name())
print(m1.set_name('new one'))