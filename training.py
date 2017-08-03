for i in 'hello world':
    if i == 'f':
        break
    print(i*2,end='')
else:
    print("^(")
l = []
lis = [1, 56, 'x', 34, 2.34, ['s', 't', 'r', 'o', 'k', 'a']]
print (lis)


l.append(23)
l.append(33)
d=[22,35]
#добавляет сиписок в список
l.extend(d)
#Всталвяет элемент 56 на номер 1 сдвигая следующие элементы
l.insert(1,56)
l.append(33)
#удалаяет первый элемент в списке, если элемента нет, возвращает ошибку
l.remove(33)
#идаляет i-тый жлемент или последный, если индекса нет
l.pop()
#Возвращщает индекс первого числа

#количество элементов в списке
l.count(33)
#сортирует список в порядке возравстания
l.sort()
l.reverse()
#очищает список
l.clear()


#__________slovar'
d1 = {'test' : 1, 'test2': "test"}
print(d1)
d2 = dict(short='dict',longer=1)
d2['short']=234
print(d2)
d3 = dict.fromkeys(['a','b'],2)
print(d3)
d4 = {a : a**2 for a in range(7)}
print(d4)
person = {'name': {'first_name':'igor','second_name':'utkin','middle_name':'igorevich'},
          'adress':['izhevsk','spb'],
          'mobile':{'first_mobile':8912,'second_mobile':8981}}
print(person['name']['second_name'])
print(person['adress'][1])
print(person['mobile']['first_mobile'])
print(person.values())

st1 = set('hello')
print(type(st1))
print(st1)
st2 = {'23', 23}
print(st2)
st3 = {i**2 for i in range(10)}
print(st3)

sst = set('hello')
fst = frozenset('frozenss')
sst.add(1)
print(sst,fst)



