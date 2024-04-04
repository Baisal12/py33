"========================Декараторы===================="
#ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА-ФУНКЦИЯБ,КОТОРАЯ ПРИНИМАЕТ В АРГУМЕНТЫ ФУНКЦИЮ ДРУГУЮ,СОЗДАЕТ ВНУТРИ СЕБЯ ФУНКЦИЮ,ВЫЗЫВАЕТ ВНУТРИ ДРУГУЮ ФУНКЦИЮ

#def func1():
#    pass

#def func2( a):# aфункцию вышего порядка так как принимает друггую функцию в аргументы
#    a()

#декараторы-функция высшего порядка,которая нужна расширить функционал функции не изменяя ее (функция обертка)


#def glushitel(func):
#    def wrapper(*args, **kwargs):
#        text = func(*args, **kwargs)
#        return text + ' тихо'
#    return wrapper
#
#def gun():
#    return 'стреляет'
#    
#a = glushitel(gun)
#result = a()
#print(result)
#print(gun())




#def glushitel(func):
#    def wrapper(*args, **kwargs):
#        text = func(*args, **kwargs)
#        return text + ' тихо'
#    return wrapper
#
#@glushitel
#def gun():
#    return 'стреляет'
#
#result = gun()
#print(result)



#from datetime import datetime
#def func_time(func):
#    def wrapper():
#        time_ = datetime.now().strftime('%d.%m.%Y %H:%M.%S')
#        print(f'оно зопустилось {time_}')
#        func()
#    return wrapper  
#
#@func_time
#def func():
#    print('hi')

#@func_time
#def func1():
#    print('hillo')

#func()
#func1()





































