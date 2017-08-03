
# try:
#     x = int(input())
# except ValueError:
#     print('Вы ввели не число')
#     x = 0
# try:
#     y = int(input())
# except ValueError:
#     print('Вы ввели не число')
#     y = 0
# #срабатывает, когда не возникает ошибки
# else:
#     print("Все верно")
#
# #срабатывает всегда
# finally:
#     print("выполнится 100 проц")
#
#
# try:
#     res = x / y
# except ZeroDivisionError:
#     print("Вы ввели 0")
#     res = 0
# print(res)

# ls = iter(range(5))
# print(type(ls))
# lg = iter([x for x in "hello"])
# print(list(lg))
# ll = [1,2,3,4,5,6]
# print(ll[0])


def f():
    try:
        yield 42
    except Exception as e:
        yield e

g = f()
print(next(g))
print(g.throw(ValueError,"something is wrong"))
print(g.throw(RuntimeError,"another error"))
