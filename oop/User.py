# class后面紧接着是类名，即User，类名通常是大写开头的单词，
# (object)，表示该类是从哪个类继承下来的
class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print('%s[%d]' % (self.name, self.age))


admin = User('admin', 20)
admin.print()
print(dir(admin))
# test = User()
# test.name = 'test'
# test.age = 23
# test.print()
