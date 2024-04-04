'===============JSON=========================='
#JavaScri


import json

#json_list = "[1,2,3,4,5]"
#python_list = json.loads(json_list)
#print(python_list)

#json_data = "null"
#python_data = json.loads(json_data)
#print(python_data)

#json_data = "true"
#python_data = json.loads(json_data)
#print(python_data)

'ДИСЕРИАЛИЗАЦИЯ - перевод c json в python обьект'
# loads - метод для десерилизации с json строки
# load - метод для десерилизации с json файла

#json_data = "false"
#python_data = json.loads(json_data)# False

#json_data = " null"
#python_data = json.loads(json_data) # None

#with open('file.sjon') as file:
    #python_data = json.load(file)
   # print(python_data)

'СЕРИЯЛИЗАЦИЯ - превод c python в json обьект'
# dumps - метод для сериализации в json строку 
# dump - метод для сериализации в json файла

#python_data = True
#son_data = json.dumps(python_data)# true
#print(json_data)

#python_data = None
#json_data = json.dumps(python_data)
#print(json_data)

#python_data = {12,4,2,5,6}
#json_data = json.dumps(python_data)
# TypeError: Object of type set is not JSON serializable
# Тип данных set нет в json формате 

#with open('file2.json', 'w') as file:
#    python_data = [12,3,4,1,None,False,True,{1:"hello", 2:"world"}]
#    json.dump(python_data, file)
   
     
 




