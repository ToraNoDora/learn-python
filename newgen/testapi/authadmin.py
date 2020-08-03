import requests


class Admin_auth:

    def __init__(self,base_url,login,password,id):
        self.url = str(base_url)
        self.session = requests.Session()
        self.tokens = {}
        self.super_admin(str(login),str(password))
        self.login_company_id(int(id))

    # Авторизация в супер-админке
    def super_admin(self, login, password):
        r = self.session.post(
        self.url + "authorizate",
        json={"login": login, "pass": password},
        headers={
                  "Authorization": "Basic OXVESTh4YTU6V1NIOHNQQ0JQTktZR2lHcml6Rmtnb3A="
                  })
        print(r.json())
        print('Статус код: {0}'.format(r.status_code))
        if r.status_code == 200:
            print('Зашли как супер-админ!')
            token = r.json()["data"]["success"]["access_token"]
            self.session.headers.update({"Authorization": "Bearer " + token})
        elif r.status_code == 404:
            print('Ресурс не найден')

    # Авторизация в компании
    def login_company_id(self, id):
        r = self.session.post(
            self.url + 'authorizate/company/' + str(id))
        print(r.json())
        if r.status_code == 200:
            print('Перешли в компанию {}'.format(id))
        elif r.status_code == 404:
            print('Ресурс не найден')
        return r.json()



