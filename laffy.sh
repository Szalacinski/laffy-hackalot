#!/bin/bash
#Sometimes sox will generate slightly different files based on the same input.
#This may make MD5sums not match occasionally over multiple runs of the script

WAV=wav/*.wav
NUM=0
for x in $WAV
do
	sox $x -r 14k -e oki-adpcm -c 1 vox/$NUM.vox gain -n 5
	NUM=$((NUM+1))
done

python3 generate_laffy_bin.py vox/*.vox > bin/laff.bin
