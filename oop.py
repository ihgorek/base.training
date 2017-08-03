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