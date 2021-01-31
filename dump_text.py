import os

try:
    os.makedirs('dialogue')
except OSError as e:
    pass
    
try:
    os.makedirs('names')
except OSError as e:
    pass

try:
    os.makedirs('system')
except OSError as e:
    pass

rom = open('POKEPICROSS.gbc', 'rb').read()

characterTable = ["あ",
"い",
"う",
"え",
"お",
"か",
"き",
"く",
"け",
"こ",
"さ",
"し",
"す",
"せ",
"そ",
"た",
"ち",
"つ",
"て",
"と",
"な",
"に",
"ぬ",
"ね",
"の",
"は",
"ひ",
"ふ",
"へ",
"ほ",
"ま",
"み",
"む",
"め",
"も",
"や",
"ゆ",
"よ",
"ら",
"り",
"る",
"れ",
"ろ",
"わ",
"を",
"ん",
"っ",
"ゃ",
"ゅ",
"ょ",
"が",
"ぎ",
"ぐ",
"げ",
"ご",
"ざ",
"じ",
"ず",
"ぜ",
"ぞ",
"だ",
"ぢ",
"づ",
"で",
"ど",
"ば",
"び",
"ぶ",
"べ",
"ぼ",
"ぱ",
"ぴ",
"ぷ",
"ぺ",
"ぽ",
"ぁ",
"ぃ",
"ぅ",
"ぇ",
"ぉ",
"ア",
"イ",
"ウ",
"エ",
"オ",
"カ",
"キ",
"ク",
"ケ",
"コ",
"サ",
"シ",
"ス",
"セ",
"ソ",
"タ",
"チ",
"ツ",
"テ",
"ト",
"ナ",
"ニ",
"ヌ",
"ネ",
"ノ",
"ハ",
"ヒ",
"フ",
"ヘ",
"ホ",
"マ",
"ミ",
"ム",
"メ",
"モ",
"ヤ",
"ユ",
"ヨ",
"ラ",
"リ",
"ル",
"レ",
"ロ",
"ワ",
"ヲ",
"ン",
"ッ",
"ャ",
"ュ",
"ョ",
"ガ",
"ギ",
"グ",
"ゲ",
"ゴ",
"ザ",
"ジ",
"ズ",
"ゼ",
"ゾ",
"ダ",
"ヂ",
"ヅ",
"デ",
"ド",
"バ",
"ビ",
"ブ",
"ベ",
"ボ",
"パ",
"ピ",
"プ",
"ペ",
"ポ",
"ァ",
"ィ",
"ゥ",
"ェ",
"ォ",
"0",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"ー",
"A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V",
"W",
"X",
"Y",
"Z",
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z",
" ",
"、",
"。",
"『",
"』",
"✕",
"“",
"”",
"!",
"?",
":",
";",
",",
".",
"·",
"(",
")",
"~",
"♂️",
"♀"]

list = []
for i in range(0,len(rom)-0x20):
	if rom[i+0] == 0x3E and rom[i+2] == 0xEA and rom[i+3] ==  0x48 and rom[i+4] == 0xD5:
		if rom[i+5] == 0x3E and rom[i+7] == 0xEA and rom[i+8] ==  0x49 and rom[i+9] == 0xD5:
			offset = rom[i+1]+((rom[i+6])<<8)
			if offset in list:
				#print('repeat')
				list.append(offset + 0x4000)
			else:
				list.append(offset + 0x4000)

count = 0
#smallest = 0xFFFF
for offset in list:
	with open('dialogue/'+str("{:03}".format(count))+'.txt', 'w+',encoding='utf8') as f:
		#if offset < smallest:
		#	smallest = offset
		#	print(hex(offset))
		#print(hex(offset))
		stop = False
		while not stop:
			if rom[offset] == 0xFF and rom[offset+1] == 0xFF:
				stop = True
			elif rom[offset] == 0xFE and rom[offset+1] == 0xFF:
				f.write('\n')
			else:
				f.write(characterTable[rom[offset]])
			offset+=2
		count+=1

base = 0x20000
table = 0x24000
count = 0
while table < 0x0241E0:
	with open('names/'+str("{:03}".format(count))+'.txt', 'w+',encoding='utf8') as f:
		offset = (rom[table] | (rom[table+1]<<8)) + (base + 2)
		if count == 43:
			print(hex(offset))
		table+=2
		stop = False
		while not stop:
			if rom[offset] == 0xFF and rom[offset+1] == 0xFF:
				stop = True
			elif rom[offset] == 0xFE and rom[offset+1] == 0xFF:
				f.write('\n')
			else:
				f.write(characterTable[rom[offset]])
			offset+=2
		count+=1

base = 0x0E4000
table = 0xE8696
count = 0
while table < 0x0E86B6:
	with open('system/'+str("{:03}".format(count))+'.txt', 'w+',encoding='utf8') as f:
		offset = (rom[table] | (rom[table+1]<<8)) + (base)
		offset1 = (rom[offset+0]) + ((rom[offset+1])<<8) + (0x4000)
		offset2 = (rom[offset+2]) + ((rom[offset+3])<<8) + (0x4000)
		table+=2
		stop = False
		while not stop:
			if rom[offset1] == 0xFF and rom[offset1+1] == 0xFF:
				f.write('\n')
				stop = True
			elif rom[offset1] == 0xFE and rom[offset1+1] == 0xFF:
				f.write('\n')
			else:
				f.write(characterTable[rom[offset1]])
			offset1+=2
		stop = False
		while not stop:
			if rom[offset2] == 0xFF and rom[offset2+1] == 0xFF:
				stop = True
			elif rom[offset2] == 0xFE and rom[offset2+1] == 0xFF:
				f.write('\n')
			else:
				f.write(characterTable[rom[offset2]])
			offset2+=2
		count+=1
