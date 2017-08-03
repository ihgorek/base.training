f = open('file.txt','w')
f.write('Hi, is\'s me\n')
f.close()
print(f.read())
for line in f:
    print(line)



#МЕНЕДЖЕРЫ КОНТЕКСТА
with acquire_resource() as r:
    do_something(r)
    #___________________________
manager = acquire_resource()
r = manager.__enter__()
try:
    do_something()
finally:
    exc_type, exc_value, tb = sys.exc_info()
    suppress = manager.__exit__(exc_type,exc_value,tb)

    if exc_value is not None and not suppress:
        raise exc_value