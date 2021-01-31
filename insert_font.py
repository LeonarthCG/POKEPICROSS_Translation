from PIL import Image

def makeFont(array,col0,col1,col2,col3):
	pixels = []
	for i in range(0,len(array)):
		for y in range(0,8):
			pixel1 = 0
			pixel2 = 0
			for x in range(0,8):
				color = array[i][y][x]
				if color == 0:
					color = col0
				elif color == 1:
					color = col1
				elif color == 2:
					color = col2
				else:
					color = col3
				pixel1 = pixel1|(((color>>0)&1)<<(7-x))
				pixel2 = pixel2|(((color>>1)&1)<<(7-x))
			pixels.append(pixel1)
			pixels.append(pixel2)
	return(pixels)

im = Image.open('font.png')
chars = []
for i in range(0,0xF3):
	chars.append([])
	for y in range(0,10):
		chars[i].append([])
		for x in range(0,16):
			chars[i][y].append(im.getpixel(((x+((16*i)%128)),(y+(10*int(i/8))))))

widths = []
for i in range(0,0xF3):
	widths.append(0)

for i in range(0,0xF3):
	for x in range(0,16):
		for y in range(0,10):
			if chars[i][y][x] != 0:
				widths[i] = x+1
	if widths[i] == 0:
		widths[i] = 1
widths[0] = 3

with open('fontWidth.event', 'w+') as f:
	f.write('ORG 0x286F\nBYTE')
	for width in widths:
		f.write(' ' + str(width))
	f.write('\n')

image = []
for i in range(0,608):
	image.append([])
	for y in range(0,8):
		image[i].append([])
		for x in range(0,8):
			image[i][y].append(im.getpixel(((x+((8*i)%128)),(y+(8*int(i/16))))))

with open('fontGraphics.event', 'w+') as f:
	f.write('ORG 0x15C000\nBYTE')
	out = makeFont(image,0,1,2,3)
	for pixels in out:
		f.write(' ' + str(pixels))
	f.write('\n')
		
	f.write('ORG 0x1B8000\nBYTE')
	out = makeFont(image,2,3,1,0)
	for pixels in out:
		f.write(' ' + str(pixels))
	f.write('\n')

	out = makeFont(image,3,2,1,0)
	f.write('ORG 0x1BC000\nBYTE')
	for pixels in out:
		f.write(' ' + str(pixels))
	f.write('\n')

