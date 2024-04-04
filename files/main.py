'=============================Модули======================'
# любой файл с раширенинием .py - модуль
# пакет - набор модулей (обязательно должен быть файл_init_.py)

'=======================работа c файломи==============='
# open - функ каторая отрывает файлы в определенном режиме 
1

'режимы'
# r - read(только для чтения)
# w - write(толькл для записи, каждый раз очищает файл и только потом записывает)
# a - append(толькл для записи, добвляет в конец)
# x - создает фыйл, но если уже существует выйдет ошибка
# b - binary (в бинарном рижиме)
 
'--------------Rea------------'
file = open('test.txt', 'r')
#print(file.read())
#ile.seek(0) # перенос коретки на начало 
#print(file.read())
#print(file.writable())
#print(file.readable())

#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())


#print(file.readlines()) #['<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>\n', 'ASDF12437\n', 'qwerasdf\n', '501501248\n', '277353\n', 'MB060708\n', '>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<']

#print(file.tell())# на каком индексе находитя каретка
#print(file.read())
#print(file.tell())

# open('qwer.txt', 'r') - Error, нет такого файла

'----------------Write------------'
file = open('py33.txt', 'w')
# если файла нет то он создаст его сам
#print(file.writable()) # True
#print(file.readable()) #False

#print(file.write('ASDF12437\n'))
#print(file.write('qwerasdf'))

#file.writelines(['hello\n', 'world\n', 'py33'])
file.close()

'----------Append------------'
file = open('new_py33', 'a')
#file.write('HELLOWORLD\n')
#ile.seek((10))
#file.write('HELLOWORLD')


'================================Контексный менеджер==============='

with open('new_py33', 'r') as file:
    print(file.read())
print(file.closed)

list1 = ['hello', 'world', 'bootcamp']
with open('test.txt', 'w') as file:
    for i in list1:
        file.write(i+'*'+'\n')





























