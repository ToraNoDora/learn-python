import re
'''
Это регулярное выражение, но в нем используется синтаксис,
которого вы не видели в регулярных выражениях .
Квадратные скобки - [] - означают «соответствуют ровно одному из этих символов».
Так [sxz]-значит «s или x, или z», но только один из них.
$ - Должны быть знакомы; это соответствует концу строки. Комбинированные,
это регулярные тесты экспрессии будь то существительное заканчивается с s, x или z.
'''
def plural(noun):
    if re.search('[sxz]$', noun):
        '''
        Эта re.sub()функция выполняет подстановки строк 
        на основе регулярных выражений
        
        Здесь вы заменяете конец строки (соответствует $) на строку es. 
        Другими словами, добавление esв строку. 
        Например noun + 'es', вы можете выполнить то 
        же самое с помощью конкатенаци строк,
        но я решил использовать регулярные выражения для каждого 
        правила по причинам, которые станут понятны позже в этой главе.
        '''
        return re.sub('$', 'es', noun)

    elif re.search('[^aeioudgkprt]h$', noun):
        '''
        Так [^aeioudgkprt] означает любой символ,
        за исключением a, e, i, o, u, d, g, k, p, r, или t.
        Затем следует этот символ, после которого h следует конец строки. 
        Вы ищете слова, которые заканчиваются на H, где H можно услышать
        '''
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):
        '''
        Слова , которые заканчиваются в Y, где символ перед Y 
        является не a , e, i, o, или u
        '''
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'


import re
# совпадает
print(re.search('[^aeiou]y$', 'vacancy'))
# boy не совпадает, потому что заканчивается oy,
# и вы специально сказали, что персонажа раньше y не могло быть o
print(re.search('[^aeiou]y$', 'boy'))
# day не совпадает, потому что это заканчивается ay
print(re.search('[^aeiou]y$', 'day'))
# не совпадает, потому что не заканчивается y
print(re.search('[^aeiou]y$', 'pita'))

import re
# Есть ли строка Mark содержит a, b или c? Да, это содержит a
print(re.search('[abc]', 'Mark'))
# Хорошо, теперь найти a, b или c, и заменить его o. Mark становится Mork
print(re.sub('[abc]', 'o', 'Mark'))
# Эта же функция превращается rock в rook.
print(re.sub('[abc]', 'o', 'rock'))
# Вы можете подумать, что это превратится caps в oaps, но это не так.
# re.subзаменяет все матчи, а не только первый.
# Таким образом, это регулярное выражение превращается caps в oops,
# потому что и the c и aget превращаются в o.
print(re.sub('[abc]', 'o', 'caps'))


print(re.sub('y$', 'ies', 'vacancy'))
print(re.sub('y$', 'ies', 'agency'))
# Просто мимоходом хочу отметить, что можно объединить эти два регулярных выражения
# (одно, чтобы узнать, применимо ли правило,
# а другое, чтобы фактически применить его) в одно регулярное выражение.
print(re.sub('([^aeiou])y$', r'\1ies', 'vacancy'))


# СПИСОК ФУНКЦИЙ
import re


def match_sxz(noun):
    return re.search('[sxz]$', noun)


def apply_sxz(noun):
    return re.sub('$', 'es', noun)


def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)


def apply_h(noun):
    return re.sub('$', 'es', noun)


def match_y(noun):
#	Теперь каждое ПРАВИЛО СООТВЕТСВИЯ является своей собственной функцией,
#	которая возвращает результаты вызова re.search()функции.
    return re.search('[^aeiou]y$', noun)

# Каждое ПРАВИЛО ПРИМЕНЕНИЯ также является своей собственной функцией,
# которая вызывает re.sub()-функцию для
# применения соответствующего правила множественного числа.
def apply_y(noun):
    return re.sub('y$', 'ies', noun)


def match_default(noun):
    return True


def apply_default(noun):
    return noun + 's'

#	Вместо того, чтобы иметь одну функцию ( plural()) с несколькими правилами,
#	у вас есть rules-структура данных,
#	которая представляет собой последовательность пар функций
rules = ((match_sxz, apply_sxz),
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default)
        )

def plural(noun):
    '''
    	Поскольку правила были разбиты на отдельные структуры данных,
    	новую plural()-функцию можно сократить до нескольких строк кода.
    	Используя for-цикл, вы можете извлечь совпадение и применить два правила за раз
    	(одно совпадение, одно применить) из структуры правил.
    	На первой итерации for-цикла, matches_rule получит match_sxz, и apply_rule
    	получит apply_sxz. На второй итерации (при условии , вы получите , что далеко),
    	matches_rule будет назначен match_h, и apply_rule будут назначены apply_h.
    	Функция гарантированно будет возвращать что-то в конце концов,
    	потому что конечное правило match ( match_default) просто возвращает True,
    	что означает соответствующее правило применения (apply_default)
    	всегда будет применяться.'''
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


# СПИСОК ШАБЛОНОВ
def build_match_and_apply_functions(pattern, search, replace):
# build_match_and_apply_functions() - это функция,
# которая динамически создает другие функции.
# Он принимает pattern, search, replace (шаблон , поиск и замену),
# а затем определяет matches_rule()-функцию ,
# которая вызывает re.search()с рисунком,
# который был передан в build_match_and_apply_functions()-функцию, и слово,
# которое передается matches_rule()-функции вы собираете
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

#
patterns = \
  (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')
  )
#  Берется последовательность строк в шаблонах и превращает их в последовательность функций.
#  Путем «сопоставления» строк с build_match_and_apply_functions()-функцией.
#  То есть он принимает каждый триплет строк и вызывает
#  build_match_and_apply_functions()-функцию с этими тремя строками в качестве аргументов.
#  build_match_and_apply_functions()-Функция возвращает кортеж из двух функций.
#  Это означает, что правила в конечном итоге становятся функционально эквивалентными
#  предыдущему примеру: список кортежей, где каждый кортеж является парой функций.
#  Первая функция - это вызывающая функция match re.search(),
#  а вторая функция - вызывающая функция apply re.sub().
rules = [build_match_and_apply_functions(pattern, search, replace)
         for (pattern, search, replace) in patterns]

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


# ФАЙЛ PATTERNS

import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

rules = []
# with-Оператор создает то , что называется контекстом : когда with-блок заканчивается,
# Python автоматически закроет файл, даже если возбуждается исключение внутри with-блока.
with open(r'C:\Users\Света\Documents\GitHub\learn-python\Closures&Generators\plural4-rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        '''
        Каждая строка в файле действительно имеет три значения, 
        но они разделены пробелами (табуляции или пробелы, это не имеет значения). 
        Чтобы разделить это, используйте split()метод строки. 
        Первым аргументом split()-метода является то None, что означает 
        «разделить на любой пробел (табуляция или пробел, это не имеет значения)». 
        Второй аргумент 3, который означает «разделить пробел 3 раза, 
        а затем оставить остальную часть строки в покое». 
        Строка вроде [sxz]$ $ es будет разбита на список ['[sxz]$', '$', 'es'], 
        что означает, что шаблон будет получен '[sxz]$', поиск получит '$', 
        а замена получит 'es'. Это большая сила в одной маленькой строчке кода.
        '''
        pattern, search, replace = line.split(None, 3)
        '''
        Наконец, вы передаете pattern, search 
        в replaceв build_match_and_apply_functions()-функцию, 
        которая возвращает набор функций. Вы добавляете этот кортеж к списку rules, 
        и rules заканчивают тем, 
        что хранят список соответствия и применяют функции, которые plural()-функция ожидает.
        '''
        rules.append(build_match_and_apply_functions(
                pattern, search, replace))
def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        print(plural(sys.argv[1]))
    else:
        print(__doc__)

# ГЕНЕРАТОРЫ #
import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return [matches_rule, apply_rule]

def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun, rules_filename='plural5-rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))

if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        print(plural(sys.argv[1]))
    else:
        print(__doc__)

# Интерактивный пример
def make_counter(x):
    print('entering make_counter')
    while True:
        '''
        Наличие yield-ключевого слова в make_counter означает, 
        что это не нормальная функция. Это особый вид функции, 
        который генерирует значения по одному за раз. 
        Вы можете думать об этом как о возобновляемой функции. 
        Его вызов вернет генератор, 
        который можно использовать для генерации последовательных значений x
        '''
        yield x
        print('incrementing x')
        x = x + 1
        '''
        Чтобы создать экземпляр make_counter-генератора, просто вызовите его, 
        как любую другую функцию. Обратите внимание, что это на самом деле 
        не выполняет код функции. Вы можете сказать это, 
        потому что первая строка make_counter()-вызывает функцию print(), 
        но ничего еще не было напечатано.
        '''
counter = make_counter(2)

next(counter)
print(make_counter)
next(counter)

next(counter)
