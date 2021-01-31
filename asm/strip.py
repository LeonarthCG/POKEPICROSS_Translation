import sys

#get the bytes
f = open(sys.argv[1], 'rb')
data = f.read()
f.close()

#find first non-0 byte
i = 0
while data[i] == 0:
    i += 1

#open the new file
f = open(sys.argv[1], 'wb')

#and write every byte after the first non-0 byte
f.write(data[i:len(data)])
