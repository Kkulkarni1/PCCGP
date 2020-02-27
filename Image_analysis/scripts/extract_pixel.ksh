#!/usr/bin/env ksh93
# Sample script to run seed_extractpixel.py on multiple files
set -o errexit
set -o nounset
# Change the input and output directories according to the requirements
INDIR=Input_images
OUTDIR1=Count_images
OUTDIR2=Pixel_text_files
OUTDIR3=mean_pixel_text_files
JOBMAX=20

for path in $INDIR/*.bmp ; do
    file=`basename $path .bmp`;
    python seed_extractpixel.py -i $path -c $OUTDIR1/$file-C.bmp -o1 $OUTDIR2/$file-pixel.txt -o2 $OUTDIR3/$file-mean_pixel.txt 
done
wait
