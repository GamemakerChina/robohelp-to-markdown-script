@echo off

set dir="workdir"

echo Deleting unnecessary files.
rd /s /q %dir%\\template
rd /s /q %dir%\\whxdata
rd /s /q %dir%\\assets\\scripts
rd /s /q %dir%\\assets\\css
rd /s /q %dir%\\assets\\fonts
del /f /s /q *.json
del /f /s /q *.js
del /f /s /q index.*
del /f /s /q index1.htm
del /f /s /q sitemap.xml

pause