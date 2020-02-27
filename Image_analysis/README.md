# This folder contains the outline for all the steps performed for image processing for replicate analysis
### Author: Roshan Kulkarni

## Analysis of seed color

###Scripts used:
* seed_extractpixel.py is a python script that extracts pixel values in RGB format from seed images

* extract_pixel.ksh is a sample shell script to run seed_extractpixel.py on mutiple images

* extract_PCA_seed_color.R is a R script that calculates the Variance and Log of Variance of PCA 1 for each RGB pixel values for accessions. 

* get_pca_color.ksh is a sample shell script to run extract_PCA_seed_color on multiple images

### Brief description of seed_extractpixel.py
* -i is a required argument that takes in input image in jpg or bmp format

* -c is an optional argument returns a jpg or bmp image with marked seeds that are detected with counts. This argument is useful to verify the threshold values for seed detection.

* -o1 is a required argument that outputs a text file with individual pixel values within each seed in an image in RGB format.

* -o2 is a required argument that outputs a text file with mean pixel values of each seed in an image in RGB format.

### Brief description of extract_PCA_seed_color.R
* -f is a required argument that takes in input text file with pixel values in RGB format

* -o is a required argument that outputs text file with variance and log of variance of pixel values in RGB format (script can be easily modified to output desired statictics like mean, std deviation and desired output format)

* Calculating PCA for pixel values of RGB format reduces the dimension of data and makes it easier for downstream processing. 
 
     
