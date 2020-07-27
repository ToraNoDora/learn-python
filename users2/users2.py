import requests
import json
import csv


class Admin_panel(object):

    def __init__(self, url):
        self.url = str(url)
        self.session = requests.Session()
        self.tokens = {}

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


    # Создание пользователей
    def create_user(self, file_obj):
        print("Создаем пользователей")

        try:
            """
            Чтение  CSV файла используя класс csv.DictReader
            """
            reader = csv.DictReader(file_obj, delimiter=',')
            for line in reader:
                data = {
                    "login": line['login'],  # Логин
                    "password": line['password'],  # Пароль
                    "phone": line['phone'],  # Телефон
                    "verified_phone": line['verified_phone'],  # Телефон подтвержден
                    "email": line['email'],  # Email
                    "verified_email": line['verified_email'],  # Email подтвержден
                    "fname": line['fname'],  # Фамилия
                    "sname": line['sname'],  # Имя
                    "chief_email": line['chief_email'],  # Email руководителя
                    "license_agree": line['license_agree'],  # Лицензионное соглашение принято
                    "is_invited": line['is_invited'],  # Пользователь приглашен
                    "is_chief": line['is_chief'],  # Пользователь является руководителем
                    "notify": line['notify'],  # Получать email-уведомления о действиях подчиненных (Если is_chief = 1)
                    "allow_skip_material": line['allow_skip_material'],
                    # Разрешить прохождение материалов в любом порядке
                    "groups": {
                        "region": line['region'],  # Регион
                        "city": line['city'],  # Город
                        "role": line['role'],  # Роль
                        "position": line['position'],  # Должность
                        "team": line['team'],  # Команда
                        "department": line['department'],  # Департамент
                        "function": line['function']  # Назначения
                    }
                }
                r = self.session.post(
                    self.url + 'user',
                    json=data,
                    headers=self.session.headers)

                if r.status_code == 422:
                    print('[Error 422] Ошибка с пользователем: {0}, json= {1}'.format(line['login'], r.json()))
                    continue
                else:
                    print("Создал пользователя id: {0}".format(r.json()['data']['id']))
            print('Создал всех пользователей из файла')
        except Exception:
            print('[Error] Что то пошло не так. Ответ сервера: {0}, json = {1}'.format(r, r.json()))


if __name__ == "__main__":
    admin = Admin_panel('https://mapi.test-eq.ru/v1/')
    admin.super_admin('login_super_admin', 'pass_super_admin')
    admin.login_company_id('1')
    csv_path = "users_csv.csv"
    with open(csv_path) as f_obj:
        admin.create_user(f_obj)

