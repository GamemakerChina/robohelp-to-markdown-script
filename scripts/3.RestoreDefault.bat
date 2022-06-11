@echo off

set dir="../workdir"

for /R %dir% %%k in (*.soup) do (
    del /f /s /q %%k
)
for /R %dir% %%k in (*.cleaned) do (
    del /f /s /q %%k
)
for /R %dir% %%k in (*.md) do (
    del /f /s /q %%k
)
del /f /s /q logs.txt
pause