import math
math.pi
print(math.pi)

# СПИСКИ
a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
print(a_list)
print(a_list[0])
print(a_list[-1])
print(a_list[-3])

# НАРЕЗКА СПИСКА
print(a_list[1:3])
print(a_list[0:3])
print(a_list[1:-1])
print(a_list[3:])
print(a_list[:])

# ДОБАВЛЕНИЕ ЭЛЕМЕНТОВ В СПИСОК
b_list = ['a']
b_list = b_list +[2.0, 3]
print(b_list)
b_list.append(True)
print(b_list)


# ПОИСК ЗНАЧЕНИЙ В СПИСКЕ
c_list = ['a', 'b', 'new', 'mpilgrim', 'new']
print(c_list.count('new'))
print('new' in c_list)
print('c' in c_list)
print(c_list.index('mpilgrim'))
print(c_list.index('new'))

# УДАЛЕНИЕ ЭЛЕМЕНТОВ СПИСКА
d_list = ['a', 'b', 'new', 'mpilgrim', 'new']
print(d_list[2])
del d_list[1]
print(d_list)
print(d_list[1])
d_list.remove('new') #удаление первого элменента в спсике с таким названием
print(d_list)

# УДАЛЕНИЕ ЭЛЕМЕНТОВ СПИСКА ЧЕРЕЗ POP
e_list = ['a', 'b', 'new1', 'mpilgrim1']
e_list.pop()
print(e_list)
e_list.pop(1)
print(e_list)

# ЛОГИЧЕСКИЙ КОНТЕКСТ СПИСКОВ
def is_it_true(anything):
    if anything:
        print("yes, it's true")
    else:
        print("no, it's false")
print(is_it_true)
print(is_it_true([0]))
print(is_it_true(['a']))

# КОРТЕЖИ
a_tuple = ("a", "b", "mpilgrim", "z", "example")
print(a_tuple)
print(a_tuple[0])
print(a_tuple[-1])
print(a_tuple[1:3])
print("z" in a_tuple)
print(a_tuple.index("example"))
# Кортежи могут быть преобразованы в списки, и наоборот. Встроенная tuple()функция принимает список и возвращает кортеж с теми же элементами, а list()функция принимает кортеж и возвращает список.
# По сути, tuple()замораживает список и list()оттаивает кортеж.
# Кортежи в логическом контексте. Примерно тоже самое, что и в списках

# НАЗНАЧЕНИЕ СРАЗУ НЕСКОЛЬКИХ ПЕРЕМЕННЫХ
v = ('a', 2, True)
(x, y, z) = v
print(x)
print(y)
print(z)
# Встроенная range()функция с назначением нескольких переменных для быстрого назначения последовательных значений
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print(MONDAY)
print(WEDNESDAY)
print(SUNDAY)

# НАБОРЫ
# Набор представляет собой неупорядоченный «мешок» уникальных значений.
# Один набор может содержать значения любого неизменяемого типа данных
# Если у вас есть два набора, вы можете выполнять стандартные операции над множествами, такие как объединение, пересечение и набор разностей

# СОЗДАНИЕ НАБОРА
a_set = {1}
print(a_set)
print(type(a_set))
a_set = {1, 3, 5}
print(a_set)
# создание набора из списка
e_list = ['a', 'b', 'mpilgrim', True, False, 42]
b_set = set(e_list)
print(b_set)
print(e_list)
# создание пустого набора
c_set = set()
print(c_set)
print(type(c_set))
print(len(c_set))
# Добавление значений в набор
d_set = {1, 3}
d_set.add(4)
print(d_set)
print(len(d_set))
d_set.update({2, 0, 6}) # все значения пойдут по логическому порядку
print(d_set)
# Удаление элементов из наборы
d_set.discard(3)
print(d_set)
d_set.remove(6)
print(d_set)
d_set.pop() # удаляет любой элемент набора
print(d_set)
d_set.clear()
print(d_set)

# СЛОВАРИ
a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print(a_dict)
print(a_dict['server'])
print(a_dict['database'])
a_dict['database'] = 'blog'
print(a_dict)
a_dict['user'] = 'dora'
print(a_dict)
a_dict['user'] = 'mark'
print(a_dict)