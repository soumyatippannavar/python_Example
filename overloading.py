class overloading:

    def sum(self, a=None, b=None, c=None):

       if a!= None and b!= None and c!= None:
           s=a+b+c

       elif a!=None and b!=None:
           s=a+b

       else:
           s=a

       return s

s = overloading()
a = int(input("enter 1st numbr"))
b = int(input("enter 2nd numbr"))
c = int(input("enter 3rd numbr"))

print(s.sum(a,b,c))