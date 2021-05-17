import requests
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content

tree = etree.parse("Welcome to Python.org.html", lxml.html.HTMLParser())

ul = tree.findall('/html/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')

for li in ul:
    a = li.find('a')
    time = li.find('time')
    print(time.get('datetime'), a.text)
