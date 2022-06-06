# coding:utf-8
from bs4 import BeautifulSoup
import sys

html_file = sys.argv[1]
html_import = open(html_file, "r", encoding='utf-8').read().encode('utf-8')
soup = BeautifulSoup(html_import, 'html.parser')

for div in soup.find_all(
    [
        {'class': ['title', 'gotohome', 'footer']},
        'title'
    ]
):
    div.decompose()

with open(html_file + ".soup.htm", "w+", encoding='utf-8') as file:
    file.write(soup.prettify())
