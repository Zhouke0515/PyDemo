import os

print(os.name)
# print(os.uname())
print(os.environ)
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
path = os.path.join(os.path.abspath('.'), 'testdir')
# 然后创建一个目录:
if not os.path.isdir(path):
    os.mkdir(os.path.join(os.path.abspath('.'), 'testdir'))
# 删掉一个目录:
# os.rmdir(os.path.join(os.path.abspath('.'), 'testdir'))
# 创建空文件
# 检验给出的路径是否真地存:os.path.exists()
file_path = os.path.join(path, 'test.txt')
if not os.path.exists(file_path):
    test_file = open(file_path, 'w')

# 返回一个路径的目录名和文件名:os.path.split()
print(os.path.split(file_path))
# 返回文件名和后缀
print(os.path.splitext(os.path.basename(file_path)))
print(os.path.getsize(file_path))
