@echo off

set dir="../workdir/whxdata"

for /R %dir% %%i in (*.new.js) do (
    python.exe ../ConvertTOC.py %%i
)
pause
