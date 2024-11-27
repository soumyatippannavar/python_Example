from abc import ABC,abstractmethod


class computer(ABC):
    @abstractmethod
    def system(self):
       pass

    @abstractmethod
    def abstac(self):
        pass

class laptop(computer):
    def system(self):
        print("abstract class")

    def abstac(self):
        print("hiiiii")

class exrta():
    def hello(self):
        print("hiiiii")

L=laptop()
L.system()
e=exrta()
e.hello()

