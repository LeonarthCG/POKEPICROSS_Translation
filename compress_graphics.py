#converts all images in the compressed folder into binary gb graphics
#afterwards, "compresses" all .bin files with the pokemon picross format

import os
import glob
from PIL import Image

files = glob.glob("compressed/*.png")

for file in files:
	im = Image.open(os.path.join(file))
	height = im.height-((im.height)%8)
	width = im.width-((im.width)%8)
	count = int(height/8)*int(width/8)
	tiles = []
	for i in range(0,count):
		tiles.append([])
		for y in range(0,8):
			tiles[i].append([])
			for x in range(0,8):
				tileh = (x+(int(((i*8)%width)/8)*8))
				tilev = (y+((int(i/int(width/8)))*8))
				tiles[i][y].append(im.getpixel(((tileh),(tilev))))
	pixels = []
	for i in range(0,len(tiles)):
		for y in range(0,8):
			pixel1 = 0
			pixel2 = 0
			for x in range(0,8):
				color = tiles[i][y][x]
				if color > 3:
					color = 3
				pixel1 = pixel1|(((color>>0)&1)<<(7-x))
				pixel2 = pixel2|(((color>>1)&1)<<(7-x))
			pixels.append(pixel1)
			pixels.append(pixel2)
	with open(file+'.bin', 'wb+') as f:
		f.write(bytes(pixels))

files = glob.glob("compressed/*.bin")
for file in files:
	f = open(file,"rb")
	data = f.read()
	compressed = []
	i = 0
	stop = False
	xor = 0
	while not stop:
		if (len(data)-i) > 0x80:
			length = 0x80
			compressed.append(0x7F)
		else:
			length = (len(data)-i)
			compressed.append((len(data)-i)-1)
			stop = True
		for j in range(0,length):
			xor = data[i]^xor
			compressed.append(xor)
			xor = data[i]
			i+=1
	with open(file+'.dmp', 'wb+') as f:
		f.write(bytes(compressed))
