class descriptor:


    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        return instance.__dict__[self.label]

    def __set__(self, instance, value):
        assert type(value) == str
        instance.__dict__[self.label] = value

# class A:
#
#     price = descriptor(2)
#
# igor = A()
# igor.price = '23'
# print(igor.price)

# class training:
#
#     def __init__(self):
#         self.d = {}
#
#     def set_less(self, lesson):
#         self.lesson = descriptor(lesson)
#
#     def get_less(self):
#         return self.lesson
#
#
# class training:
#     def __init__(self, fget=None, fset=None, fdel=None, doc=None):
#         self.fget = fget
#         self.fset = fset
#         self.fdel = fdel
#         self.__doc__ = doc
#
#     def __get__(self, obj, objtype=None):
#         if obj is None:
#             return self
#
#         if self.fget is None:
#             raise AttributeError("нечитаемый атрибут")
#
#         return self.fget(obj)
#
#     def __set__(self, obj, value):
#         if self.fset is None:
#             raise AttributeError("не могу установить атрибут")
#
#         self.fset(obj, value)
#
#     def __delete__(self, obj):
#         if self.fdel is None:
#             raise AttributeError("не могу удалить атрибут")
#
#         self.fdel(obj)



