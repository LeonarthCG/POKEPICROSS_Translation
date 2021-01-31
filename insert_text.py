import os
import glob

rom = open('POKEPICROSS_ENG.gbc', 'rb').read()

characterDict = {
" ": 0,
"!": 1,
"\"": 2,
"️♂": 3,
"♀": 4,
"%": 5,
"&": 6,
"\'": 7,
"(": 8,
")": 9,
"*": 10,
"+": 11,
",": 12,
"-": 13,
".": 14,
"/": 15,
"0": 16,
"1": 17,
"2": 18,
"3": 19,
"4": 20,
"5": 21,
"6": 22,
"7": 23,
"8": 24,
"9": 25,
":": 26,
";": 27,
"<": 28,
"=": 29,
">": 30,
"?": 31,
"@": 32,
"A": 33,
"B": 34,
"C": 35,
"D": 36,
"E": 37,
"F": 38,
"G": 39,
"H": 40,
"I": 41,
"J": 42,
"K": 43,
"L": 44,
"M": 45,
"N": 46,
"O": 47,
"P": 48,
"Q": 49,
"R": 50,
"S": 51,
"T": 52,
"U": 53,
"V": 54,
"W": 55,
"X": 56,
"Y": 57,
"Z": 58,
"[": 59,
"\\": 60,
"]": 61,
"^": 62,
"_": 63,
"\'": 64,
"a": 65,
"b": 66,
"c": 67,
"d": 68,
"e": 69,
"f": 70,
"g": 71,
"h": 72,
"i": 73,
"j": 74,
"k": 75,
"l": 76,
"m": 77,
"n": 78,
"o": 79,
"p": 80,
"q": 81,
"r": 82,
"s": 83,
"t": 84,
"u": 85,
"v": 86,
"w": 87,
"x": 88,
"y": 89,
"z": 90,
"{": 91,
"|": 92,
"}": 93,
"~": 94,
"‘": 113,
"’": 114,
"“": 115,
"”": 116,
"•": 117,
"–": 118,
"—": 119,
"¡": 129,
"¿": 159,
"é": 207}

files = glob.glob("dialogue_eng/*.txt")

list = []
for i in range(0,len(rom)-0x20):
	if rom[i+0] == 0x3E and rom[i+2] == 0xEA and rom[i+3] ==  0x48 and rom[i+4] == 0xD5:
		if rom[i+5] == 0x3E and rom[i+7] == 0xEA and rom[i+8] ==  0x49 and rom[i+9] == 0xD5:
			if i in list:
				#print('repeat')
				list.append(i)
			else:
				list.append(i)

offset = 0x9C68
widths = 0x286F
with open('dialogue.event','w+') as dialogue:
	for file in files:
		id = str(file[len(file)-7]) + str(file[len(file)-6]) + str(file[len(file)-5])
		with open(file,'r',encoding='utf8') as f:
			out = "ORG " + str(list[int(id)]+1) + "; BYTE " + str((offset&0x3FFF)&0xFF) + "; ORG " + str(list[int(id)]+6) + "; BYTE " + str(((offset&0x3FFF)>>8)+0x40) + "\n"
			text = f.read().splitlines()
			width = 0
			for line in range(0,len(text)):
				newwidth = 0
				for char in text[line]:
					number = 0
					if char == "♂":
						number = 3
					elif char == "♀":
						number = 4
					else:
						number = characterDict[char]
					newwidth+=rom[widths+number]+1
				if newwidth > width:
					width = newwidth-1
			if width > 144:
				print('too big')
				print(id)
			out = out + "ORG " + str(offset) + "; BYTE"
			for line in range(0,len(text)):
				for char in text[line]:
					if char == "♂":
						out = out + " 3"
					elif char == "♀":
						out = out + " 4"
					else:
						out = out + " " + str(characterDict[char])
					offset+=1
				if len(text) > 1:
					if line+1 != len(text):
						out = out + " 0xFE"
						offset+=1
			out = out + " 0xFF\n"
			offset+=1
		dialogue.write(out)

files = glob.glob("system_eng/*.txt")

list = []
for i in range(0,len(rom)-0x20):
	if rom[i+0] == 0x3E and rom[i+2] == 0xEA and rom[i+3] ==  0x48 and rom[i+4] == 0xD5:
		if rom[i+5] == 0x3E and rom[i+7] == 0xEA and rom[i+8] ==  0x49 and rom[i+9] == 0xD5:
			if i in list:
				#print('repeat')
				list.append(i)
			else:
				list.append(i)

list = []
base = 0x0E4000
table = 0xE8696
i = 0
while table < 0x0E86B6:
	list.append([])
	list[i].append((rom[table+0] | (rom[table+1]<<8)) + (base))
	list[i].append((rom[table+0] | (rom[table+1]<<8)) + (base + 2))
	i+=1
	table+=2

widths = 0x286F
with open('system.event','w+') as system:
	for file in files:
		id = str(file[len(file)-7]) + str(file[len(file)-6]) + str(file[len(file)-5])
		with open(file,'r',encoding='utf8') as f:
			text = f.read().splitlines()
			for line in range(0,len(text)):
				out = "ORG " + str(list[int(id)][line]) + "; BYTE " + str((offset&0x3FFF)&0xFF) + " " + str(((offset&0x3FFF)>>8)+0x40) + "\n"
				width = 0
				newwidth = 0
				for char in text[line]:
					number = 0
					if char == "♂":
						number = 3
					elif char == "♀":
						number = 4
					else:
						number = characterDict[char]
					newwidth+=rom[widths+number]+1
				if newwidth > width:
					width = newwidth-1
				if width > 144:
					print('too big (system)')
					print(id)
				out = out + "ORG " + str(offset) + "; BYTE"
				for char in text[line]:
					if char == "♂":
						out = out + " 3"
					elif char == "♀":
						out = out + " 4"
					else:
						out = out + " " + str(characterDict[char])
					offset+=1
				if len(text) > 1:
					if line+1 != len(text):
						out = out + " 0xFF"
						offset+=1
				out = out + " 0xFF\n"
				offset+=1
				system.write(out)

if offset > 0xC000:
	print('went past bank!')

files = glob.glob("names_eng/*.txt")
table = 0x24000
offset1 = 0x241E0
offset2 = 0x27320
limit = 0x25000
widths = 0x286F
with open('names.event','w+') as names:
	for file in files:
		id = str(file[len(file)-7]) + str(file[len(file)-6]) + str(file[len(file)-5])
		with open(file,'r',encoding='utf8') as f:
			if offset1 < limit:
				curr = offset1
			else:
				curr = offset2
			out = "ORG " + str(table+(int(id)*2)) + "; SHORT " + str(0x4000 + (curr - 0x24000)) + "\n"
			text = f.read().splitlines()
			width = 0
			for line in range(0,len(text)):
				newwidth = 0
				for char in text[line]:
					number = 0
					if char == "♂":
						number = 3
					elif char == "♀":
						number = 4
					else:
						number = characterDict[char]
					newwidth+=rom[widths+number]+1
				if newwidth > width:
					width = newwidth-1
			if rom[0xFC000+(rom[0x100000+int(id)+int(id)])+((rom[0x100001+int(id)+int(id)])<<8)] > 0:
				if width >= 92:
					print('big')
					print(id)
				out = out + "ORG " + str(curr) + "; BYTE (0x60 +" + str(int((64 - width)/2)) + ") 0" #96
			else:
				if width >= 60:
					print('small')
					print(id)
				out = out + "ORG " + str(curr) + "; BYTE (0x60 +" + str(int((64 - width)/2)) + ") 0"
			curr+=2
			for line in range(0,len(text)):
				for char in text[line]:
					if char == "♂":
						out = out + " 3 0"
					elif char == "♀":
						out = out + " 4 0"
					else:
						out = out + " " + str(characterDict[char]) + " 0"
					curr+=2
				if len(text) > 1:
					if line+1 != len(text):
						out = out + " 0xFE 0xFF"
						curr+=2
			out = out + " 0xFF 0xFF 0\n"
			curr+=3
			if offset1 < limit:
				offset1 = curr
			else:
				offset2 = curr
		names.write(out)
		
if curr > 0x28000:
	print('went past bank!')
