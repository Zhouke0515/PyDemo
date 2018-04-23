import math

print(abs(1))
print(abs(-1))

# abs(1,2)

print(bool(1))
print(int(2.1))
print(str(123))

# 函数名其实就是指向一个函数对象的引用，
# 完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-1))
print(str(hex(5)))


# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
def fun(x):
    # isinstance()进行数据类型检查
    if not isinstance(x, (int)):
        raise TypeError()
    size = 1
    while (size < x):
        size <<= 1;
    # print(x)
    return size


print(fun(9))


# 空函数
def empty_fun():
    return


def empty_fun2():
    pass


# 返回多个值
# Python的函数返回多值其实就是返回一个tuple，但写起来更方便
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)
print(x, y)
print(r)


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('参数必须是整数或小数')
    if not isinstance(b, (int, float)):
        raise TypeError('参数必须是整数或小数')
    if not isinstance(c, (int, float)):
        raise TypeError('参数必须是整数或小数')
    if a == 0:
        raise ValueError('第一个参数不能为0')
    delt = math.pow(b, 2) - (4 * a * c);
    if delt < 0:
        print('方程无实数根，但有2个共轭复根。')
        raise ValueError('方程无实数根，但有2个共轭复根')
    elif delt == 0:
        print('方程有两个相等的实数根。')
    else:
        print('方程有两个不相等的实数根。')
    x1 = (-b + math.sqrt(delt)) / (2 * a)
    x2 = (-b - math.sqrt(delt)) / (2 * a)
    return x1, x2


a, b = quadratic(1, 6, 5)
print(a, b)


# 可变参数函数
def calc(*nums):
    sum = 0
    for num in nums:
        sum += num;
    return sum


print(calc(1, 3, 5))
