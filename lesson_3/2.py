from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db = client['wonderful_herschel']
vacancy = db.vacancy


def function_1(value):
    for item in vacancy.find({}):
        if item['compensation'] is None:
            pass
        elif ['minimum', 'maximum', 'currency'] == list(item['compensation'].keys()):
            if item['compensation']['currency'] == 'руб':
                if item['compensation']['minimum'] < value < item['compensation']['maximum']:
                    print(item)
            if item['compensation']['currency'] == 'USD':
                if item['compensation']['minimum'] < value/60 < item['compensation']['maximum']:
                    print(item)
            if item['compensation']['currency'] == 'EUR':
                if item['compensation']['minimum'] < value/62 < item['compensation']['maximum']:
                    print(item)
            if item['compensation']['currency'] == 'KZT':
                if item['compensation']['minimum'] < value*7.43 < item['compensation']['maximum']:
                    print(item)
        elif ['minimum', 'currency'] == list(item['compensation'].keys()):
            if item['compensation']['currency'] == 'руб':
                if item['compensation']['minimum'] > value:
                    print(item)
            if item['compensation']['currency'] == 'USD':
                if item['compensation']['minimum'] > value / 60:
                    print(item)
            if item['compensation']['currency'] == 'EUR':
                if item['compensation']['minimum'] > value / 62:
                    print(item)
            if item['compensation']['currency'] == 'KZT':
                if item['compensation']['minimum'] > value * 7.43:
                    print(item)
        elif ['maximum', 'currency'] == list(item['compensation'].keys()):
            if item['compensation']['currency'] == 'руб':
                if value < item['compensation']['maximum']:
                    print(item)
            if item['compensation']['currency'] == 'USD':
                if value/60 < item['compensation']['maximum']:
                    print(item)
            if item['compensation']['currency'] == 'EUR':
                if value/62 < item['compensation']['maximum']:
                    print(item)
            if item['compensation']['currency'] == 'KZT':
                if value*7.43 < item['compensation']['maximum']:
                    print(item)


function_1(200000)
