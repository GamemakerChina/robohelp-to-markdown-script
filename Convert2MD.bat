@echo off

set dir="workdir"

for /R %dir% %%i in (*.htm) do (
    python.exe soup.py %%i
    echo Soupped %%i
)
for /R %dir% %%j in (*.soup) do (
    python.exe clean.py %%j
    echo Cleaned %%j
)
for /R %dir% %%k in (*.cleaned) do (
    python.exe %%k
    echo Converted %%k
)
pause
