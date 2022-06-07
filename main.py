# coding:utf-8
from lxml.html.clean import Cleaner
from bs4 import BeautifulSoup
import sys
import os

html_file = os.path.splitext(sys.argv[1])[0]

def soupManual(htmlfile):
    html_import = open(htmlfile + ".htm", "r", encoding='utf-8').read()
    html_replace_br = html_import.replace('<br/>', '')
    soup = BeautifulSoup(html_replace_br, 'html.parser')
    for div in soup.find_all("div", {'class': ['title', 'gotohome', 'footer', 'rh-hide']}):
        div.decompose()

    for others in soup.find_all(["title"]):
        others.decompose()

    for code in soup.find_all("p", {'class': ['code']}):
        code.replace_with('<pre><code class="language-gml">' + code.string + '</code></pre>')

    with open(htmlfile + ".soup", "w+", encoding='utf-8') as file:
        file.write(soup.prettify().replace('&lt;', '<').replace('&gt;', '>'))

def cleanManual(soupfile):
    soup_import = open(html_file + ".soup", "r", encoding='utf-8').read().encode('utf-8')
    safe_attrs = frozenset(['src', 'a', 'href', 'pre', 'code'])

    remove_tags = frozenset([
        'div', 'p', 'title', 'h5'
    ])

    cleaner = Cleaner(
        safe_attrs=safe_attrs,
        remove_tags=remove_tags,
        scripts=True,
        style=True,
        meta=True,
        page_structure=False
    )
    cleaned_html = cleaner.clean_html(soup_import)

    soup = BeautifulSoup(cleaned_html, 'html.parser')

    for code in soup.find_all("pre"):
        code.replace_with('<pre><code class="language-gml">' + code.string + '</code></pre>')

    with open(soupfile + ".cleaned", "w+", encoding='utf-8') as file:
        file.write(soup.prettify().replace('&lt;', '<').replace('&gt;', '>'))

def convertManualToMarkdown(cleanedfile):
    os.system("pandoc -f html " + cleanedfile + ".cleaned -o " + os.path.splitext(cleanedfile)[0] + ".md")

soupManual(html_file)
cleanManual(html_file)
convertManualToMarkdown(html_file)
print("Completed: " + html_file + ".htm")
