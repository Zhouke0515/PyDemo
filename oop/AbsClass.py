import abc


class AbsClass(metaclass=abc.ABCMeta):
    def __init__(self):
        self.__name = 'abs_class'

    @abc.abstractmethod
    def abs_method(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class ChildClass(AbsClass):
    pass
    # def __init__(self):
    # super.__init__()


class ChildClass2(AbsClass):
    # 子类不重写__init__，实例化子类时，会自动调用父类定义的__init__
    # 为了能使用或扩展父类的行为，最好显示调用父类的__init__方法
    def __init__(self):
        super(ChildClass2, self).__init__()
        self.name = 'child_class'

    def abs_method(self):
        print('实现了抽象方法')


# 抽象类不能实例化
# abs = AbsClass()
# abs.abs_method()
# 子类不实现抽象方法，也不能实例化
# child = ChildClass()
# child.abs_method()
child2 = ChildClass2()

child2.abs_method()
print(child2.name)
child2.name = 'test'
print(child2.name)
