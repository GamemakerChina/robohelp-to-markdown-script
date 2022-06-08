@echo off

set dir="workdir"

for /R %dir% %%i in (*.htm) do (
    python.exe main.py %%i
)
pause
