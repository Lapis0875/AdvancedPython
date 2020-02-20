# 함수룰 다른 함수의 인자로 전달할 수 있다!
def my_function(func, value):
    return func(value)


def test(value):
    return value+1


result = my_function(test, 5)
print(f'result = {result}')