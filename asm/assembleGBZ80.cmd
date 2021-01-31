rgbasm.exe -o %~n1.elf %~1
rgblink.exe -x -o %~n1.bin %~n1.elf
del %~n1.elf
strip.py %~n1.bin
