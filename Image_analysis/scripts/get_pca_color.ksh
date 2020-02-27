#!/usr/bin/env ksh93
# This is a sample code to run extract_PCA_seed_color.R on multiple files
set -o errexit
set -o nounset

INDIR=mean_pixel_text_files/Select_het
OUTDIR=pca_seed_color/Select_het
JOBMAX=20

for path in $INDIR/*.txt ; do
    file=`basename $path -mean_pixel.txt`;
    Rscript extract_PCA_seed_color.R -f $path -o $OUTDIR/$file-pca.txt 
done
wait
