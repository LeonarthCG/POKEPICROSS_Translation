cd %~dp0
copy POKEPICROSS.gbc POKEPICROSS_ENG.gbc

insert_font.py

cd "%~dp0Event Assembler"

ColorzCore A FE8 "-output:%~dp0POKEPICROSS_ENG.gbc" "-input:%~dp0fontWidth.event"

cd %~dp0
convert_graphics.py
compress_graphics.py
insert_text.py
MAKE_HACK.cmd
