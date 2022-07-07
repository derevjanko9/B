import pymongo
from pymongo import MongoClient
from pymongo import errors
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re

client = MongoClient('127.0.0.1', 27017)
db = client['wonderful_herschel']
vacancy_collection = db.vacancy

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
url = 'https://krasnodar.hh.ru/search/vacancy'
params = {'search_field': 'name', 'text': 'Python', 'page': 0, 'hhtmFrom': 'vacancy_search_list'}
session = requests.Session()
while True:
    response = session.get(url=url, params=params, headers=headers)
    dom = BeautifulSoup(response.text, 'html.parser')
    vacancy = dom.find_all('div', {'class': 'vacancy-serp-item__layout'})
    if len(vacancy) == 0:
        break
    params['page'] += 1
    for item in vacancy:
        vacancy_data = {}
        block_a = item.find('a', {'class': 'bloko-link'})
        href = block_a.get('href')
        name = block_a.text
        compensation = item.find('span', {'class': 'bloko-header-section-3'})
        if compensation:
            compensation = compensation.text
        vacancy_data['name'] = name
        vacancy_data['href'] = href
        vacancy_data['website'] = 'hh.ru'
        dict_1 = {}
        item_1 = (str(compensation)).replace('\u202f', '')
        if item_1[0].isdigit():
            re_minimum_maximum = re.compile(r'\d+')
            re_currency = re.compile(r'\w+')
            minimum = re_minimum_maximum.findall(item_1)[0]
            maximum = re_minimum_maximum.findall(item_1)[1]
            currency = re_currency.findall(item_1)[-1]
            dict_1['minimum'] = int(minimum)
            dict_1['maximum'] = int(maximum)
            dict_1['currency'] = currency
            vacancy_data['compensation'] = dict_1
        if item_1[0] == 'о':
            re_minimum_maximum = re.compile(r'\d+')
            re_currency = re.compile(r'\w+')
            minimum = re_minimum_maximum.findall(item_1)[0]
            currency = re_currency.findall(item_1)[-1]
            dict_1['minimum'] = int(minimum)
            dict_1['currency'] = currency
            vacancy_data['compensation'] = dict_1
        if item_1[0] == 'д':
            re_minimum_maximum = re.compile(r'\d+')
            re_currency = re.compile(r'\w+')
            maximum = re_minimum_maximum.findall(item_1)[0]
            currency = re_currency.findall(item_1)[-1]
            dict_1['maximum'] = int(maximum)
            dict_1['currency'] = currency
            vacancy_data['compensation'] = dict_1
        if item_1 == 'None':
            vacancy_data['compensation'] = None
        if vacancy_collection.find_one({'href': vacancy_data['href']}):
            pass
        else:
            vacancy_collection.insert_one(vacancy_data)

print(len(list(vacancy_collection.find({}))))
for item in vacancy_collection.find({}):
    print(item)
