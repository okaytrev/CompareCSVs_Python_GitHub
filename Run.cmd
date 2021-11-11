@echo off

SET mypath=%~dp0

gam group all-managers@hopin.to print > %mypath%Google.csv

python.exe "%mypath%CompareCSVs.py"

gam csv "%mypath%CSV_Differences.csv" gam update group all-managers@hopin.to add member ~"Hopin Email"  user 

pause