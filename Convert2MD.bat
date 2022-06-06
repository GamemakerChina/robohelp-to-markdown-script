@echo off

set dir="workdir"

for /R %dir% %%i in (*.htm) do (
    python.exe soup.py %%i
    echo Soupped %%i
)
for /R %dir% %%j in (*.soup.htm) do (
    python.exe clean.py %%j
    echo Cleaned %%j
)
for /R %dir% %%k in (*.cleaned.htm) do (
    pandoc %%k -o %%k.md
    echo Converted %%k
)
pause
