# 클래스 내부에서 더하기, 빼기 등의 각종 연산자의 실행 결과를 정의할 수 있다!
class MyClass:
    # Integer
    i: int = None

    # String
    s: (str or list) = None

    def __init__(self, i: int = 0, s: (str or list) = ''):
        self.i = i
        self.s = s

    # '+' 연산자 정의
    def __add__(self, other):
        if type(other) == MyClass:
            return MyClass(self.i+other.i, self.s+other.s)

        elif type(other) == int:
            return MyClass(self.i+other, self.s)

        elif type(other) == str:
            return MyClass(self.i, self.s+other)

        else:
            raise ArithmeticError(f'Cannot add {type(other)} to {type(self)}')

    # '-' 연산자 정의
    def __sub__(self, other):
        if type(other) == MyClass:
            return MyClass(self.i-other.i, self.s.replace(other.s, ''))

        elif type(other) == int:
            return MyClass(self.i-other, self.s)

        elif type(other) == str:
            return MyClass(self.i, self.s.replace(other, ''))

        else:
            raise ArithmeticError(f'Cannot substarct {type(other)} to {type(self)}')

    # '*' 연산자 정의
    def __mul__(self, other):
        if type(other) == MyClass:
            return MyClass(self.i*other.i, self.s+'*'+other.s)

        elif type(other) == int:
            return MyClass(self.i*other, self.s)

        elif type(other) == str:
            return MyClass(self.i, self.s+'*'+other)

        else:
            raise ArithmeticError(f'Cannot multiply {type(other)} and {type(self)}')

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

    # '**' 연산자 정의
    def __pow__(self, power, modulo=None):
        if type(power) is MyClass:
            return MyClass(self.i**power.i, self.s+'**'+power.s)
        elif type(power) is int or float:
            return MyClass(self.i**power, self.s)
        elif type(power) is str:
            return MyClass(self.i, self.s+'**'+power.s)
        else:
            raise ArithmeticError(f'Cannot pow {type(self)} with {power}')

    # if MyClass() 했을때 True인가 False인가?
    def __bool__(self):
        if self.i is not None or self.s is not None:
            return True
        else:
            return False

    def getData(self):
        return f'self.i = {self.i}, self.s = {self.s}'


# 기본정보 표시
print('-'*20)
a = MyClass(i=5, s='Hello a!')
b = MyClass(i=10, s='Goodbye b!')
n = 5
s = 'o'
f = 2.1
print(f'a = ({a.getData()}), b = ({b.getData()}), \nn = {n}, s = {s}, f = {f}')

if a:
    print('a is True')
if b:
    print('b is True')

# + 연산 결과 확인하기
print('-'*20)
print('+ 연산')
print(' 가능한 예시들 : ')
print(f'a+b = {(a+b).getData()}')
print(f'a+n = {(a+n).getData()}')
print(f'b+n = {(b+n).getData()}')
print(f'a+s = {(a+s).getData()}')
print(f'b+s = {(b+s).getData()}')
print(' 불가능한 예시들 : ')
#print(f'a+True = {(a+True).getData()}')
#print(f'a+f = {(a+f).getData()}')

# - 연산 결과 확인하기
print('-'*20)
print('- 연산')
print(' 가능한 예시들 : ')
print(f'a-b = {(a-b).getData()}')
print(f'a-n = {(a-n).getData()}')
print(f'b-n = {(b-n).getData()}')
print(f'a-s = {(a-s).getData()}')
print(f'b-s = {(b-s).getData()}')
print(' 불가능한 예시들 : ')
#print(f'a-True = {(a-True).getData()}')
#print(f'a-f = {(a-f).getData()}')

# * 연산 결과 확인하기
print('-'*20)
print('* 연산')
print(' 가능한 예시들 : ')
print(f'a*b = {(a*b).getData()}')
print(f'a*n = {(a*n).getData()}')
print(f'b*n = {(b*n).getData()}')
print(f'a*s = {(a*s).getData()}')
print(f'b*s = {(b*s).getData()}')
print(' 불가능한 예시들 : ')
#print(f'a*True = {(a*True).getData()}')
#print(f'a*f = {(a*f).getData()}')

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

# ** 연산 결과 확인하기
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
