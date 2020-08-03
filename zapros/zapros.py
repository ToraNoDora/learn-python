import requests
import classfile
import json
'''
datas = {
    
}
'''
'''
def auth(url,login,password):
    json = {'company_id': 0, 'login': iriglava, 'pass': qwerty123}
    header = {'Authorization':'Basic OXVESTh4YTU6V1NIOHNQQ0JQTktZR2lHcml6Rmtnb3A='}
    responce = requests.post(url, json = json, headers = header)
    #print(responce.json()['success']['access_token'])
    #print('Статус код: {0}'.format(responce.status_code)
    return responce.json()['success']['access_token']
    responce = requests.get(url, headers = header)

def get_course(url, token):
    header = {'Authorization':'Bearer' + str(token)}
    requests.get(url, headers = header)
    token = aut()


 if __name__ == '__main__':
     auth('https://api.test-eq.ru/v25/auth','iriglava', 'qwerty123')
     #get_course('', token)
'''



'''
response = requests.get('https://manager.test-eq.ru/login')
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

# Упрощение через оператор if
if response:
    print('Success!')
else:
    print('An error has occurred.')

response = requests.get('https://manager.test-eq.ru/login')
# указываем необходимую кодировку
response.encoding = 'utf-8'
print(response.text)

print(response.headers['Content-Type'])

# Поиск местонахождения для запросов на GitHub
response = requests.get(
    'https://api.github.com/search/repositories',
    params = {'q': 'requests+language:python'},
)

# Анализ некоторых атрибутов местонахождения запросов
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+
'''
def auth(url,login,password):
    json = {"company_id": 0, "login": login, "pass": password}
    header = {"Authorization": "Basic OXVESTh4YTU6V1NIOHNQQ0JQTktZR2lHcml6Rmtnb3A="}
    responce = requests.post(url, json=json, headers=header)
    print(responce.json())
    print('Статус код: {0}'.format(responce.status_code))
    return responce.json()['success']['access_token']

def get_courses(url,token):
    header = {"Authorization": "Bearer " + str(token)}
    responce = requests.get(url, headers=header)
    print(responce.json())
    print('Статус код: {0}'.format(responce.status_code))

if __name__ == "__main__":
    token = auth('https://api.test-eq.ru/v25/auth','iriglava','qwerty123')
    get_courses('https://api.test-eq.ru/v25/trainings',token)