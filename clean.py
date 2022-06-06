# coding:utf-8
from lxml.html.clean import Cleaner
from bs4 import BeautifulSoup
import sys
import os

html_file = sys.argv[1]
html_import = open(html_file, "r", encoding='utf-8').read().encode('utf-8')

safe_attrs =  frozenset(['src', 'a', 'href'])

remove_tags = frozenset([
    'div', 'p', 'title'
])

cleaner = Cleaner(
    safe_attrs=safe_attrs,
    remove_tags=remove_tags,
    scripts=True,
    style=True,
    meta=True,
    page_structure=True
)

cleaned_html = cleaner.clean_html(html_import)

soup = BeautifulSoup(cleaned_html, 'html.parser')

with open(os.path.splitext(html_file)[0] + ".cleaned", "w+", encoding='utf-8') as file:
    file.write(soup.prettify())
