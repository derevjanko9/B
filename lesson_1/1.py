import requests
import json

url = 'https://api.github.com/users/derevjanko9/repos'
response = requests.get(url)
list_repos = [item['name'] for item in response.json()]

with open('repos.json', 'w', encoding='utf-8') as f_n:
    list_as_string = json.dumps(list_repos, indent=4)
    f_n.write(list_as_string)
