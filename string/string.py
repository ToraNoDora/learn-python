# СТРОКИ
s = '深入 Python'
print(len(s))
print(s[0])
print (s + ' 3')

# ФОРМАТИРОВАНИЕ СТРОК
username = 'mark'
password = 'PapayaWhip'
# {0} и {1} замена полей, которые заменяются аргументами , переданными к format()методу
print("{0}'s password is {1}".format(username, password))

# СТРОКИ И БАЙТЫ
by = b'abcd\x65'
print(by)
print(type(by))
print(len(by))
by += b'\xff'
print(by)
print(len(by))
print(by[0])


