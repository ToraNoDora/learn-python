import csv
import requests

from testapi.authadmin import Admin_auth

class Generation(Admin_auth):

    def __init__(self):
        super(Generation, self).__init__('https://mapi.test-eq.ru/v1/','your_login', 'your_password','your_id')

    def create_user(self, file_obj):

        print("Начинаем создавать пользователей")

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
