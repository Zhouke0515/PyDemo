# 对于单个字符的编码，
# Python提供了ord()函数获取字符的整数表示，
# chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('汉'))
# print(ord("a汉0"))

print(chr(48))
print(chr(91))
print(chr(27720))

x = b'abc'
print(x)
# str通过encode()方法可以编码为指定的bytes
print('abc'.encode('ASCII'))
# print('中文'.encode('ASCII'))
print('中文'.encode('UTF-8'))
# 要把bytes变为str，就需要用decode()方法
print(b'abc'.decode('ASCII'))

# str包含多少个字符，可以用len()函数
print('ab')
print('中文')
# 换成bytes，len()函数就计算字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 格式化输出字符串
print('Hello %s' % 'World')
print('%s,你的号码是：%d' % ('cc', 5321))

# format
print('{0} + {1} = {2}'.format(1, 3, 4))
print('Hello, {name}'.format(name='zk'))
print('Hello, {name}. Your score:{score}'.format(name='zk', score=55))


def str_format(str):
    str = str.replace(' ', '')
    return str


print('https:忘/记/pan这.baidu.事com的/我s/1Rom唉llNOYr1P凑UOL5IiKu字DoQ数')
