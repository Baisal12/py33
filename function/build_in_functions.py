'=================Втроенные функции================'
# map, filter, reduce, zip, enumerate

'ZIP'
# cоздает несколько последовотельностей(получаем генератор, в котором элементы tuple)

#list1 = [1,2,3,4]
#list2 = ['a', 'b', 'c', 'd']
#list3 = [10.5, 20.6, 35.8, 0.5]

#zipped = zip(list1, list2, list3)
#print(list(zipped)) # list[tuple, tuple, tuple]
#print(dict(zipped)) # dict немолжет сладывоть больше 2 элементов dict{k:v, k:v, k:v}



'ENUMERATE'
#нумерует последовательность erate object at 0x74b5e8087f40>
#print(list(enumerated)) # [(0,(по дефолту с 0)(тоже возвращает генеротор)
#enumerated = enumerate('hello', 1) # [(1, 'h'), (2, 'e'), (3, 'l'), (4, 'l'), (5, 'o')]
#enumerated = enumerate('hello') #<enum 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

#for i in enumerated:
 #   print(i)

#(0, 'h')
#(1, 'e')
#(2, 'l')
#(3, 'l')
#(4, 'o')

#enum = enumerate([12, 8, 'hi', True, 'HELLO', None])
#print(list(enum))   #[(0, 12), (1, 8), (2, 'hi'), (3, True), (4, 'HELLO'), (5, None)]



'MAP'
# принимает другую функ и последовательностью map прмнемает функ, которую передали на каждый элемент из последовательности. возвращает map генератор

#list_ = [1,2,3,4]
#def func(a):
#    return str(a)

#mapped = map(func, list_)
#print(mapped) #<map object at 0x75473cab3c10>
#print(list(mapped)) #['1', '2', '3', '4']



#list1 = [1,2,3,4]
#def func(a):
#    return a ** 2

#mapped = map(func, list1)
#print(list(mapped))


'lambda - это одноразовая онанимная функ '

#list_ = [1,2,3,4]
#mapped = map(lambda num1: num1 ** 2, list_)
#print(list(mapped))


'FILTER'
# принемает другую функ и последовательность, применяет функ которую мы передали на каждый элемент последовательности и остовляет тольео те элементы которую прошли проверку

#list1 = [-10, 0, 39, -12, -3, 23, 1, 0]
#def func(a):
#    return a >= 0

#b = filter(func, list1)
#print(list(b))

#filtered = filter(lambda a: a >= 0, list_1)
#print(list(filtered))   
 

#list1 = [1,2,3,4,5,6,7,8]
#def func(a):
#    return a % 2 == 0

#filtered = filter(func, list1)
#print(list(filtered))

'REDUCE'
# принемает функ и последовательность, возврощает 1 элемент (передавая функб должена передовать 2 аргумента)
from functools import reduce

list1 = [12, 3, 6, 5, 8]
print(reduce(lambda a, b: a + b, list1))



my_dict = {'старый_ключ': 'старое_значение'}

# Используем метод update() для добавления нового ключа и значения
my_dict.update({'новый_ключ': 'новое_значение'})

print(my_dict)



