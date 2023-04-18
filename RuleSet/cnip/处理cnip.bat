@echo off

setlocal enabledelayedexpansion

set INPUTFILE=cnip.txt
set OUTPUTFILE=cnip.yaml

echo payload:>> %OUTPUTFILE%

for /f "tokens=* delims=" %%a in (%INPUTFILE%) do (
  set LINE=  - IP-CIDR,%%a,no-resolve
  echo !LINE!>> %OUTPUTFILE%
)

echo "Done!"
