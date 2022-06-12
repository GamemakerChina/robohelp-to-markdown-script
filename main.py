# coding:utf-8
import time
from lxml.html.clean import Cleaner
from bs4 import BeautifulSoup
import sys
import os
import re
import urllib
import urllib.request
from PIL import Image
from io import StringIO, BytesIO

html_file = os.path.splitext(sys.argv[1])[0]

Local_Assets = "http://localhost:8080/assets/"

Manual_Assets_Mirror = "https://gms.magecorn.com/Manual/assets/"

def soupManual(htmlfile):
    html_import = open(htmlfile + ".htm", "r", encoding='utf-8').read()
    html_replace_br = html_import.replace('<br/>', '')
    soup = BeautifulSoup(html_replace_br, 'html.parser')
    for div in soup.find_all("div", {'class': ['title', 'gotohome', 'footer', 'rh-hide']}):
        div.decompose()

    for title in soup.find_all("title"):
        title.decompose()

    for code in soup.find_all("p", {'class': ['code']}):
        new_soup = BeautifulSoup(str(code), 'html.parser')
        for uselessTags in new_soup.find_all(["strong", "span", "br"]):
            uselessTags.unwrap()

        code.replace_with('<pre><code class="language-gml">' + str(new_soup) + '</code></pre>')

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
        new_soup = BeautifulSoup(str(code), 'html.parser')
        for uselessTags in new_soup.find_all(["p", "pre", "code"]): # Remove excess tags
            uselessTags.unwrap()

        code.replace_with('<pre><code class="language-gml">' + str(new_soup.prettify()).replace("    ", "") + '</code></pre>')

    for image in soup.find_all("img"):
        image.attrs['src'] = (Local_Assets + image.attrs['src'])
        image.attrs['src'] = re.sub(".*/assets/", Local_Assets, image.attrs['src'], 0)
        image_size = urllib.request.urlopen(image.attrs['src']).read()
        image_tmp = BytesIO(image_size)
        img = Image.open(image_tmp)
        print(max(img.size))
        if max(img.size) >= 10 and max(img.size) <= 60:
            image.replace_with(str(image))
        else:
            image.replace_with('<br/>' + str(image) + '<br/>')

    for image in soup.find_all("img"):
        image.attrs['src'] = (Manual_Assets_Mirror + image.attrs['src'])
        image.attrs['src'] = re.sub(".*/assets/", Manual_Assets_Mirror, image.attrs['src'], 0)

    with open(soupfile + ".cleaned", "w+", encoding='utf-8') as file:
        file.write(soup.prettify().replace('&lt;', '<').replace('&gt;', '>'))

def convertManualToMarkdown(cleanedfile):
    os.system("pandoc -f html " + cleanedfile + ".cleaned -o " + os.path.splitext(cleanedfile)[0] + ".md -t gfm")

if sys.argv[2] == "--all":
    soupManual(html_file)
    cleanManual(html_file)
    convertManualToMarkdown(html_file)

if sys.argv[2] == "--clean-html":
    soupManual(html_file)
    cleanManual(html_file)


with open("logs.txt", "a+", encoding='utf-8') as logs:
    print("Converting: " + html_file + ".htm", file=logs)
    print("Completed: " + html_file + ".htm", file=logs)
