class Example:
    name='abcd'

    def __init__(self):
            self.name='ramya'

    def update(self):
        return self.name

E=Example()
print(E.update())
E.name='soumya'
print(E.update())
print(Example.name)

