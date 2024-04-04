'=========================Exceptions====================='
# Исключения - обьект, который прерывает работу кода, если не было обработаны

SyntaxError
#исключение, которое выходит, когда в коде допущенна синтаксическая ошибка 

'''
a =
SyntaxError
'''

NameError
# исключения, которая выходит когда мы обращаемся к несуществующей переменной 


'''
num1 = 15
print(num2)
NameError
'''


IndexError
#исключения, которая выходит, когда мы обращаемся по не существуещему инденсу

'''
list_ [21, 12, 3, 1]
print(list_(1000))
IndexError: list index out of range
'''

'''
[12, 2, 14, 53, 29, 23].pop(100)
IndexError: list index out of range
'''

'''
[].pop()
IndexError: pop from empty list
'''

KeyError
# исключениБ котрорая выходит когда мы обращаемся по не сущ ключу

'''
a = {'a':1, 'b':2}
b = ['c']
KeyError:
'''

'''
dict_ = {'a':1}
dict_.get('c')
ошибки не будет Так как get не вызывоет ошобку.
'''

ValueError
# исключения, выходит когда мы передаем в функ не коррктный для нее тип данных
# когда мы расспаковываем итреррируемяй обьект на несколько переменных и кол-во переменных не совпадает с кол-во элентов

'''
int('10bfh')
ValueError:
'''

'''
a, b, c = 2, 3
ValueError:
'''

TypeError
# исключение выходит, когда мы пытаемся использать методы к какомута типу данных 
# когда мы пытаемся передать фун больше или меньше аргументов чем принемает фун

'''
for i in 1234:
    ...
TypeError:
'''
'''
'5' + 5
TypeError:
'''
'''
{[1,2,3]:'hi'}
TypeError:
'''

'''
input('введите число' 123)
TypeError:
'''
'''
[].append()
TepyError:
'''

ZeroDivisionError

'''
45 / 0
ZeroDivisionError:
'''

'''
23//0
ZeroDivisionError:
'''

'''
12%0
ZeroDivisionError:
'''

AttributeError
# выходит когда мы обращаемя к несуществуещему аттребуту или методу обьекта 

'''
[1,23,1,56].replace('a', '')
AttributeError:
'''
'''
'makers'.pop(0)
AttributeError:
'''


IndentationError

'''
    a = 3
IndentationError:
'''

'''
for i in range(11):
print(i)
IndentationError:
'''

ExceptionTypeError
# исключения которые создали, чтобы его вызывать 

'===========Вызов искл========================'

#raise NameError('просто ты тупой')

'=================Обработка исключения================'
# что-бы код не прекрощал работу сваю работу,мы можем использовть конструкцию rty-except, и обрабатываеть вызванное исключение

#try:
#    num =int(input('число: '))
#except ValueError:# ожидаемую искл
#    #Обработку на искл которого поймали
#    print('просто ты пупой')
#else:
#    #код который отрабатывает если искл не вышло
#    print(f'вы ввели число {num}')
#finally:
#    # работает всегда
#    print('ты все равно тупой')

#try:
#    num = int(input('x'))
#    res = 10 / num
#except Exception:
#    print('ты тупой?')

# except: обрабатывоет все искл моторые могут выйти
####################################################################
# except Exception: обрабатывоет все искл моторые могут выйти

# можем указывать в except несколько искл при помощи скобок и запятой except()

#try:
#    raise NameError
#except NameError:
#    print(1)


try:
    number = float(input("Введите число: "))
    if number > 0:
        raise ValueError("Положительное число")
    elif number < 0:
        raise ("Отрицательное число")
    else:
        raise ZeroDivisionError("0")
except:
    print()

























