# coding:utf-8
import sys
import os

html_file = sys.argv[1]
os.system("pandoc -f html " + html_file + " -o " + os.path.splitext(html_file)[0] + ".md")
