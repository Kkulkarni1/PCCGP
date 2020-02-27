#!/usr/bin/Rscript
# This script takes in text with mean pixel values in RGB format and returns variance ond log of variance of PCA1 for each RGB pixel values for accessions.  
# Author: Roshan Kulkarni
# Usage: Rscript extract_PCA_seed_color.R -f input.txt -o output-PCA.txt
# Importing necessary packages
library(optparse)
library(dplyr)

# Constructing argument parser
option_list = list(
  make_option(c("-f", "--file"), type="character", default=NULL, 
              help="dataset file name", metavar="character"),
  make_option(c("-o", "--out"), type="character", default="out.txt", 
              help="output file name [default= %default]", metavar="character")
); 

opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);
if (is.null(opt$file)){
  print_help(opt_parser)
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
}
args = commandArgs(trailingOnly=TRUE)

# Reading input file
temp_PCA_DF <- read.table(opt$file, header = TRUE)
IN_FILE <- opt$file
file_suffix <- gsub(pattern="\\-mean_pixel.txt$","", IN_FILE)
num_vars = which(sapply(temp_PCA_DF, class)=="numeric")

# Calculating PCA
temp.pca <- prcomp(temp_PCA_DF[,c(3:5)], center = TRUE, scale. = TRUE)
summary(temp.pca)
PCA_df <- temp.pca$x
# Selecting PCA 1
PCA_df_PC1 <- subset(PCA_df, select = PC1)
temp.pca$rotation
#Mean_1 <- mean(PCA_df_PC1)
var_1 <- var(PCA_df_PC1)
log_var_1 <- log(var_1)
#Mean_1 <- as.data.frame(Mean_1)
var_1 <- as.data.frame(var_1)
log_var_1 <- as.data.frame(log_var_1)
#Mean_1 <- mutate(Mean_1, File_name = file_suffix)
var_1 <- mutate(var_1, File_name = file_suffix)
log_var_1 <- mutate(log_var_1, File_name = file_suffix)
#Mean_1 <- Mean_1[c(2,1)]
#log_var_1 <- log_var_1[c(2,1)]

# Writing output files
write.table(data.frame(var_1, log_var_1), file=opt$out, row.names=FALSE, sep="\t")
