class MyClass:
    # Integer
    i: int = None

    # String
    s: (str or list) = None

    def __init__(self, i: int = 0, s: (str or list) = ''):
        self.i = i
        self.s = s

    # '/' 연산자 정의
    def __truediv__(self, other):
        if type(other) == MyClass:
            return MyClass(int(self.i/other.i), self.s.split(other.s))

        elif type(other) == int:
            return MyClass(int(self.i/other), self.s)

        elif type(other) == str:
            return MyClass(self.i, self.s.split(other))

        elif other == 0:
            raise ZeroDivisionError

        else:
            raise ArithmeticError(f'Cannot divide {type(self)} into {type(other)}')

# 기본정보 표시
print('-'*20)
a = MyClass(i=5, s='Hello a!')
b = MyClass(i=10, s='Goodbye b!')
n = 5
s = 'o'
f = 2.1
print(f'a = ({a.getData()}), b = ({b.getData()}), \nn = {n}, s = {s}, f = {f}')

# / 연산 결과 확인하기
print('-'*20)
print('/ 연산')
print(f'a/b = {(a/b).getData()}')
print(f'a/n = {(a/n).getData()}')
print(f'b/n = {(b/n).getData()}')
print(f'a/s = {(a/s).getData()}')
print(f'b/s = {(b/s).getData()}')
print(' 불가능한 예시들 : ')
#print(f'a/True = {(a/True).getData()}')
#print(f'a/f = {(a/f).getData()}')
print(f'a/0 = {(a/0).getData()}')