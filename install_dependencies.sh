#!/bin/bash

mkdir -p bin

## Tabix, bgzip
echo Installing TABIX
git clone https://github.com/samtools/htslib.git
cd htslib
git checkout 1.3.2
make
cp tabix bgzip ../bin
cd ..

## vcfkeepsamples
echo Installing VCFlib
git clone --recursive https://github.com/vcflib/vcflib.git
cd vcflib
git checkout v1.0.0-rc1
make
cp bin/vcfkeepsamples ../bin
cd ..

## bcftools
echo Installing BCFtools
git clone https://github.com/samtools/bcftools.git
cd bcftools
git checkout 1.3.1
make
cp bcftools ../bin
cd ..

# vcftools
echo Installing VCFtools
git clone https://github.com/vcftools/vcftools.git
cd vcftools
git checkout v0.1.14
./autogen.sh
./configure
make
cp src/cpp/vcftools ../bin
cd ..

# bedtools
echo Installing BEDtools
git clone https://github.com/arq5x/bedtools2.git
cd bedtools2
git checkout v2.26.0
make
cp bin/bedtools bin/intersectBed ../bin
cd ..

# libBigWig
echo Installing libBigWig
git clone https://github.com/dpryan79/libBigWig.git
cd libBigWig
make
cd ..

# htslib
echo Installing HTSlib
git clone https://github.com/samtools/htslib.git
cd htslib 
git checkout 1.9
make
cd ..

# GSL
echo Installing GSL
wget ftp://www.mirrorservice.org/sites/ftp.gnu.org/gnu/gsl/gsl-latest.tar.gz 
tar -xvzpf gsl-latest.tar.gz
cd gsl*
./configure
make
cd ..

# Wiggletools
echo Installing Wiggletools
git clone https://github.com/Ensembl/WiggleTools.git
cd WiggleTools
make
cp bin/wiggletools ../bin
cd ..

# bigBedToBed
echo Installing bigBedToBed
mkdir -p bigBedToBed
cd bigBedToBed
wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bigBedToBed

# pybedtools v0.7.8, requests, pandas
pip install pybedtools==0.7.4 requests pandas flask cherrypy

# ld_vcf from ensembl-variation
gcc -Wall -O3 C/ld_vcf.c -I htslib -o bin/ld_vcf -Lhtslib -Wl,-rpath,htslib -lhts -lm

# h5py
pip install h5py==2.8.0

#sqlite
pip install pysqlite
