'=====================словри==================='
# dict - изменяемый, итерируемый, неупорядочный (псевдопорядок)тип данных, для хранения данных в парах{ключь:знпчение}

#user = {'name':'Anonym', 'age':30, 'last_name':'Makers'}
#print(user['name']) #Anonym
#print(user['age']) #30
#print(user['last_name']) #Makers

# ключами в словаре могут быть не изменяемые типы данных
# ключи в словарях должны быть уникальным

'=========================сознание словарей========================'
#dict_ = {'a':1, 'b':1}
#dict_ = dict({('a',1),('b',2)})
#print(dict_)
#dict_ = dict(['a1', 'b2', 'c3'])
#print(dict_) 

#dict_ = {}
#dict_['name'] = 'makers'
#dict_['age'] = 50  
#dict_['last_name'] = 'bootcamp'
#print(dict_)     


'===================================Методы словаря========================='


'get - метот который получае значения по клбчю если указанного ключа нет выходит None-по по умачания можем его поменять'

#user = {'name':'Anonym', 
 #   'age':15, 
  #  'last_name':'Makers'}
#print(user.get('nam'))
#print(user.get('id', 'Такого ключа нету'))

#pop - удаления элемента из списка по индексу но также возвращает удаленный элемент

#dict_ = {'a':1, 'b':2, 'c':3}
#popped = dict_.pop('b')
#print(dict_)
#print(popped)


'popiten - удаяет последнее значения пару и возврвщает ee'
#dict_ = {'a':1, 'b':2, 'c':3}
#popped = dict_.popitem()
#print(dict_) # {'a':1, 'b':2}

'update - расшираяет словарь парами из второго словаря'

#dict_1 = {1:'a', 2:'a'}
#dict_2 = {2:'b', 3:'b'}
#dict_1.update(dict_2)
#print(dict_1) #{1: 'a', 2: 'b', 3: 'b'}

'clear - очищает словарь'
#dict_ = {'a':1, 'b':2, 'c':3}
#dict_.clear()
#print(dict_)#{}

'fromkeays - метод для сосдания нового словаряб ипользуя список навых'
#dict_ = dict.fromkeys('hi')
#print(dict_)
#dict_2 = dict.fromkeys(['hi', 123, True], 0)
#print(dict_2) #{'hi': 0, 123: 0, True: 0}

'keys, valus, items'
#keys - метот который возвращает все ключи
#valus - метот который возвращает все значения
#items - метот который возвращает пары ключь и значение в виде tuple

#user = {
   # 'name':'Anonym',
    #'age':15,
    #'last_name':'Makers'
#}

#print(user.keys()) #dict_keys(['name', 'age', 'last_name'])
#print(user.values()) #dict_values(['Anonym', 15, 'Makers'])
#print(user.items()) #dict_items([('name', 'Anonym'), ('age', 15), ('last_name', 'Makers')])

'===============================итерирование словарей======================'
#user = {
 #   'name':'Anonym',
  #  'age':15,
   # 'last_name':'Makers'
#}

#for i in user:
 #   print(i) # приходит ключь

#for valuse in user.values():
#    print(valuse) #приходит значения

#for item in user.items():
#    print(item) #приходит tuple с ключем и значениям

'------------------------------------------------------'
#dict_1 = {1:'a', 2:'b'}
#dict_2 = {}
#for a, b in dict_1.items():
    #dict_2[b] = a
    #print(dict_2)

# Метод setdefault() для словарей в Python используется для получения значения по указанному ключу. Если ключ не существует в словаре, setdefault() добавляет ключ со значением, переданным вторым аргументом, и возвращает это значение. Если ключ уже существует, метод просто возвращает текущее значение этого ключа.









































































































































































































