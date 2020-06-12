# laffy-hackalot
Scripts to generate custom images for Laffy Laffalot

Module ID:

Toys that use the same module or a similar module as this toy may work with these scripts with slight modifications.

HOWTO:

`mkdir bin vox wav`

`chmod +x laffy.sh`

`cd ch341prog` (flashrom can be used if preferred)

`make`

`cd ..`


Backup the default sounds:

`ch341prog/ch341prog -r bin/backup.bin`

Fill the wav directory with exactly 20 wav files.
Use Audacity to make sure the clips have a *very* consistent amplitude throughout.
The toy doesn't like lower volumes, and can jump between extremely quiet and extremely loud.

Generate the .vox and .bin files:

`./laffy.sh`

Write the bin file to Laffy:

`ch341prog/ch341prog -w bin/laff.bin`

If you find that the clips are too distorted, simply remove the `gain -n 5` from laffy.sh


CH341 programmer: (AFFILIATE LINK)
