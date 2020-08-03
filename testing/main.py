from testapi.generation import Generation

if __name__ == "__main__":
    # u_login = str(input('Введите логин от суперадминки: '))
    # u_password = str(input('Введите пароль от суперадминки: '))
    # admin.super_admin(u_login, u_password)
    #  u_id = str(input('Введите id компании: '))
    # admin.login_company_id(u_id)
    csv_path = "users_csv.csv"
    with open(csv_path) as f_obj:
        Generation().create_user(f_obj)