# f = open(r'C:\Users\Sven\Desktop\test.txt', 'r')

# 关于open 模式：
#
# w 以写方式打开，
# a 以追加模式打开 (从 EOF 开始, 必要时创建新文件)
# r+ 以读写模式打开
# w+ 以读写模式打开 (参见 w )
# a+ 以读写模式打开 (参见 a )
# rb 以二进制读模式打开
# wb 以二进制写模式打开 (参见 w )
# ab 以二进制追加模式打开 (参见 a )
# rb+ 以二进制读写模式打开 (参见 r+ )
# wb+ 以二进制读写模式打开 (参见 w+ )
# ab+ 以二进制读写模式打开 (参见 a+ )
try:
    f = open(r'C:\Users\Sven\Desktop\test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open(r'C:\Users\Sven\Desktop\test.txt', 'r') as f:
    print('1', f.read())

with open(r'C:\Users\Sven\Desktop\test.txt', 'r') as f:
    print('2', f.read(1024))

with open(r'C:\Users\Sven\Desktop\test.txt', 'r') as f:
    line = f.readline()
    while line:
        print('3', line.strip())
        line = f.readline()

with open(r'C:\Users\Sven\Desktop\test.txt', 'r') as f:
    for line in f.readlines():
        print('4', line)

with open(r'C:\Users\Sven\Desktop\test.txt', 'r') as f:
    for line in f:
        print('5', line.strip())
