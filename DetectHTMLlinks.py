import re


if __name__ == '__main__':
    n = int(input())
    p = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'
    for _ in range(n):
        html = input()
        r = re.findall(p, html)
        for link, title in r:
            print("\n{},{}".format(link, title. strip()))