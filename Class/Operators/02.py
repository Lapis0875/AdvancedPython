class Example01:
    i: int = 0

    def __init__(self, i: int=0):
        self.i = i

    def get_data(self):
        print(f'self.i = {self.i}')


a = Example01(i=5)
b = Example01(i=10)
print(a+b)
print(type(a+b))