age2=800
class variables:
  age1=21

  def __init__(self, age):
    self.age2 = age


  def setup(self):
       print(self.age1)
       print(self.age2)


v1 = variables(20)
v2 = variables(30)
v1.age2 = 40
#variables.age1 = 33
print(v1.age2, v1.age1)
print(v2.age2, v2.age1)
print(globals()['age2'])
v1.setup()