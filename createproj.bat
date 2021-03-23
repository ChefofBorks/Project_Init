@echo on

set vw=%1
set pn=%2
cd /d %~dp0


python main.py %vw% %pn%


    