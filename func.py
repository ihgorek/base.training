# def func(x):
#     def add(a):
#         return x+a
#     return add
#
# test = func(100)
# print(test(200))
# def nw(**args):
#     return args
# print(nw(a=2,b=22))
#
# add = lambda w, x: x + w
# print(add(1,3))
# print((lambda w, x: x + w)(2,4))

#
# def app(l=[]):
#     l.append(1)
#     print(l)
# app()
# app()
# def app2(l=None):
#     l = [] if l is None else l
#     l.append(2)
#     print(l)
# app2()
# app2()

def train (*args,**kwargs):
    for i,arg in enumerate(args):
        print("Аргументы такие: {0} - {1}".format(i,arg))
    for key in kwargs:
        print("keyword argument {0} = {1}".format(key, kwargs[key]))

l = [1,2,3,4,5,6,7,8,9]
d = dict(name = 'igor', surmane = 'utkin', age = 21 )
print(l)
f= open('file.txt','rb')
print(d,file=f)
train(*l,**d)







