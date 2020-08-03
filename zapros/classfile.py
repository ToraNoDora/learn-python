import requests



def auth(url,login,password):
    json = {"company_id":0,"login": login,"pass": password}
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