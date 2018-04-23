# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']

def name_format(name):
    if not isinstance(name, str):
        raise TypeError("必须是字符串类型")
    format_name = ""
    for i, ch in enumerate(name):

        ascii_num = ord(ch)
        if i == 0:
            # 小写变大写
            if 97 <= ascii_num <= 122:
                ch = chr(ascii_num - 32)
        else:
            # 大写变小写
            if (ascii_num >= 65) and (ascii_num <= 90):
                ch = chr(ascii_num + 32)
        format_name = format_name + ch

    return format_name


print(name_format("adam"))
names = list(map(name_format, ["admin", "Test", 'adam', 'LISA', 'barT']))
print(names)
for name in names:
    print(name)
