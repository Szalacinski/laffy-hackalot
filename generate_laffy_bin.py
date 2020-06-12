#!/usr/bin/python3

#A quick and dirty script to generate bin files for Laffy Laffalot
import struct
import sys
import os

if len(sys.argv[1:]) != 20:
	sys.stderr.write('ERROR: Need exactly 20 .vox files\n')
	quit()

# Generate start and end pointers for audio clips.
# The clip's end pointer functions as the next clip's start pointer 
# We start writing audio at 0x100
bin = bytearray([0xF8,0x00,0x01,0x00])
position = 4
file_position = 0x100

for x in sys.argv[1:]:
	bin += bytes([0xF8])
	file_len = os.path.getsize(x)
	file_position += file_len
	buf = struct.pack('<Q', file_position)
	bin += bytes(buf[:3])
	position += 4
	
# We don't want any of the key pointers to be overwritten
if file_position > 0x17F000:
	sys.stderr.write('ERROR: Files too large\n')
	quit()

while position < 0x100:
	bin += bytes([0xFF])
	position += 1

# Append .vox files to the bin
for x in sys.argv[1:]:
	in_file = open(x, "rb")
	bin += in_file.read()
	in_file.close()
	
position = file_position

while position < 0x17F000:
	bin += bytes([0xFF])
	position += 1
	
# The pointer structure to user-recorded clips through the microphone
# 0xF8 *clip start address* 0xFF *clip end address*
bin += bytes([0xF8, 0x00, 0x00, 0x18, 0xFF, 0x01, 0x00, 0x18,
              0xF8, 0x00, 0x00, 0x1A, 0xFF, 0x01, 0x00, 0x1A,
              0xF8, 0x00, 0x00, 0x1C, 0xFF, 0x01, 0x00, 0x1C,
              0xF8, 0x00, 0x00, 0x1E, 0xFF, 0x01, 0x00, 0x1E])
position += 32

while position < 0x200000:
	bin += bytes([0xFF])
	position += 1
	
sys.stdout.buffer.write(bin)
