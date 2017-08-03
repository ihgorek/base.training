g = [1,2,3,4,5,6,7,8,'y','t','r']
c = [a + b for a in 'list' if a!= 's' for b in 'sopu' if b!= 'p']
print(c)
d = [a + str(b) for a in 'hayat' if a!='t' for b in range(8) if b!= 7]
r = [x+' - its string!' if type(x)==str else str(x) + ' - ist int!'  for x in g]
gen = (x for x in range(8))
print(next(gen))
print(next(gen))
first_list = [x +" " if type(x)==str else x**2
              for x in g
              ]
second_list = [
    x
    for x in range(len(g))
]
print(first_list)
print(second_list)
#Функция zip сливает элеметы с одним индексом в один элемент
ans = zip(second_list,first_list)
print(list(ans))


#Функция map вызывает функцию на каждый элемент списка
#выводить будет это
#[2, 4, 6, 8, 10, 12, 14]
def f (x):
    return x+x
items = [1,2,3,4,5,6,7]
squared = map(f,items)
print(list(squared))


#Функция filter почти как мап, но с одним условием, она выводит только элементы с True
#будет выводить это
#[-5, -4, -3, -2, -1]
number_list = range(-5,5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)


#lambda - это сокращенный фид функции
#def f(x, y):
#    if (y == None):
#        y = 1
#    return x*y
#записывается так: lambda x, y: x * (y if y is not None else 1)
#Получается это функция с одним действием

#Можно взять первый и последний элемент зоть чего с помощью среднего жлемента, который будет брать все сотальное в себя
first,*rest,last = range(1,5)
print(first)
print(rest)
print(last)

#ГЕНЕРАТОРЫ
class Backwards:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


backwards = Backwards('some')
iter(backwards)  # < Backwards instance at 0x7fceac135c68 >
for char in backwards:
    print(char)  # e m o s




