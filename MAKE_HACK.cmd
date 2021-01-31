cd %~dp0

copy POKEPICROSS.gbc POKEPICROSS_ENG.gbc

cd "%~dp0Event Assembler"

ColorzCore A FE8 "-output:%~dp0POKEPICROSS_ENG.gbc" "-input:%~dp0ROM_Buildfile.event"

cd %~dp0

rgbfix -v POKEPICROSS_ENG.gbc

cd "%~dp0ups"

ups diff -b "%~dp0POKEPICROSS.gbc" -m "%~dp0POKEPICROSS_ENG.gbc" -o "%~dp0POKEPICROSS_ENG.ups"

pause
