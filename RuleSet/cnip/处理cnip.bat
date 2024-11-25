@echo off

setlocal enabledelayedexpansion

set INPUTFILE=.\RuleSet\cnip\merge.txt
set OUTPUTFILE=cnip.yaml

echo payload:>> %OUTPUTFILE%

for /f "tokens=* delims=" %%a in (%INPUTFILE%) do (
  set LINE=  - IP-CIDR,%%a
  echo !LINE!>> %OUTPUTFILE%
)

echo "Done!"
