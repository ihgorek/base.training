# class Employee:
#     salary = 0
#     def computeSalary(self):
#         pass
#
#     def giveRaise(self):
#         pass
#
#     def promote(self):
#         pass
#
#     def retire(self):
#         pass
#
# class Engineer(Employee):
#
#     def computeSalary(self):
#         pass
#
# params = [x for x in range(6) if x!=3]
# assert all(map(lambda p: p>=0,params))
# d = map(lambda p: p>=0,params)
# print(list(d))
#
# class A:
#     def __getattr__(self, item):
#         return item
#
# print(A().foo)



class Something:
    attr = 42


name, bases, attrs = "Some_else", (), {"attr":42}
Some_else = type (name, bases, attrs)
print(Something)
print(Some_else)


#Foo = type('Foo', (), {'bar':True})
#   Это одно и то же
# class Foo(object):
# ...       bar = True


# метаклассу автоматически придёт на вход те же аргументы,
# которые обычно используются в `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    Возвращает объект-класс, имена атрибутов которого
    переведены в верхний регистр
  """

  # берём любой атрибут, не начинающийся с '__'
  attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
  # переводим их в верхний регистр
  uppercase_attr = dict((name.upper(), value) for name, value in attrs)

  # создаём класс с помощью `type`
  return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr # это сработает для всех классов в модуле

class Foo(object):
  # или можно определить __metaclass__ здесь, чтобы сработало только для этого класса
  bar = 'bip'


print(hasattr(Foo, 'bar'))
# Out: False
print(hasattr(Foo, 'BAR'))
# Out: True

f = Foo()
print(f.BAR)
# Out: 'bip'
# А теперь то же самое только используя настоящий класс
class UpperAttrMetaclass(type):

    def __new__(cls, name, bases, dct):

        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        return type.__new__(cls, name, bases, uppercase_attr)