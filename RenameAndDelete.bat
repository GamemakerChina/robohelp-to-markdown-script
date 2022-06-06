@echo off

set dir="workdir"

ren %dir%\\*.htm.soup.htm.cleaned.htm.md *.md

@REM Command from Git for Windows
@REM sleep 5 

@REM for /R %dir% %%k in (*.htm) do (
@REM     del /f /s /q %%k
@REM )
pause