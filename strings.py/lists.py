'===================List=============='
# списки изменяемый, индексируемый, упорядочный, итерируемый тип данных, предназначен для хранения любых данных в определенном порятке 

list_1 = [1, 2, 14, 'hello', True, [0,0,0], None]

list_1[3]
list_1[-1]
list_1[-2][-1]
list_1[3][-2]
list_1[5]

# range(start , end(не вкл)), step - функция генеротор который генерирует\зоздает диапозон от start до end(не вкл)

list_2 = list(range(0, 101))
#print(list_2)
#print(list(range(50, 71)))

print(list(range(1, 11, 2)))

'======================Методы списков======================='
# append - для дополннения элементов в коней списка 

list_ = []
list_.append(1)
list_.append('hello world')
list_.append(True)
#print(list_) # [1, hello world True]

'pop - удаления элемента из списка по индексу но также возвращает удаленный элемент'

list3 = [23, 32, 24, 34]
popped = list3.pop(1)
#print(list3)
#print(popped)

'remove - удаления элемента из списка по значению'

list_ = [23, 3, 34, 35, 53]
list_.remove(53)
#print(list_)



'count - чтитает кол-во применяемых элементов в списке'

#list_ =  [1, 1, 1, 12, 1, 13, 42, 1, 872262]
#print(list_.count(1))

'index - возвращает индекс первого вхождения принятого элемента'

list_ = ['hi', 1, 234, 301, 8913, 'hello world', 'hi']
#print(list_.index('hello world'))


'extent - расширяет список при помощи другого списка'

#list_1 = [1,2,3]
#list_2 = [0,0,0]
#list_1.append(list_2)
#list_1.extend(list_2)
#print(list_1)



'reverse - изменяет список, растав его элементы в обратном порятки '

list_ = [1, 2, 3, 4, 5, 6, 7]
list_.reverse()
#print(list_)


'sort - сортирует список, сост элементов одного типа'
list_ = [12, 3, 13, 8319, 26]
list_.sort()
#print(list_)

list_ = ['c', 'b', 'a', 'A', 'B']
list_.sort()
#print(list_)


'clear - удаляет все'
list_ = [1, 2, 3, 4, 5, 6, 6, 7, 8, 123456678]
list_.clear()
#print(list_)

list_ = ['картошка', 'лук', 'лук', 'картошка', 'лук']

paket1 = []
paket2 = []
for ruka in list_:
    if ruka == 'картошка':
        paket1.append(ruka)
    elif ruka == 'лук':
        paket2.append(ruka)

#print(paket1)
#print(paket2)








































































































































































































































































































































































































































































































































































































































































































































































































































































































































