from bs4 import BeautifulSoup
import requests

source = 'https://ru.stackoverflow.com/'
html = requests.get(source).content
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', id = 'question-mini-list')
a = div.find_all('a', class_='question-hyperlink')

for i in a:
    print(i.getText(), source + i.get('href'))

a_for_parent = div.find('a', class_='question-hyperlink')
parent = a_for_parent.find_parent()
print('This is a parent:', parent)