'''
1. Получить html-код страницы
2. Получить карточки c товарами из html-кода
3. Распарсить даннные из какрточки (стягивать данные из кактрочек)
4. Получить данные записать в файл(csv)
'''

import requests

from bs4 import BeautifulSoup as bs                                  

url = 'https://enter.kg/computers/noutbuki_bishkek'

def get_html(url):
    html = requests.get(url)
    return html.text

def get_cards(html):
    soup = bs(html,'lxml')
    laptops = soup.find_all('div', class_='row')
    return laptops

def get_data(list_):
    data = []
    for laptop in list_:
        data.append({
            'title':laptop.find('span',class_='prouct_name').text,
            'price':laptop.find('span',class_='price').text,
            'image':'https://enter.kg/'+laptop.find('img').get('src') #может быть ошибка
            })     
    return data




def get_last_paga(html):
    soup = bs(html, 'lxml')
    link = links[-1]
    if link.text.strip() == 'В конец':
        return True
    else:
        return False 

def main(url):
    count = 0
    while True:
        URL = f'{url}/results,{count}01-{count}00'
        html = get_html(URL)
        laptops = get_cards(html)
        data = get_data(laptops)
        flag = get_last_paga(html)
        if not flag:
            break
        count += 1
        print(f'Парсинг страницы{count}')

main(url)


#import csv

#csv_file = 'file.csv'
#with open(csv_file, 'w', newline='', encoding='utf-8') as file:
#    writer = csv.DictWriter(file, fieldnames=data[0].key())
#    writer.writeheader()
#    for laptop in data:
#        writer.writerow(laptop)

#print(csv_file)
