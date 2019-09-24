## Create Jeme_ENCODE
for e in {1..127}; do echo http://yiplab.cse.cuhk.edu.hk/jeme/encoderoadmap_lasso/encoderoadmap_lasso.${e}.csv >> Jeme_ENCODE.txt; done
## Create Jeme_FANTOM5
for e in {1..808}; do echo http://yiplab.cse.cuhk.edu.hk/jeme/fantom5_lasso/fantom5_lasso.${e}.csv >> Jeme_FANTOM5.txt; done
## Create CAPE_eQTL
for e in E003 E004 E005 E006 E007 E008 E017 E021 E022 E029 E032 E034 E046 E050 E055 E056 E059 E080 E084 E085 E089 E090 E091 E092 E093 E094 E097 E098 E100 E109 E114 E116 E117 E118 E119 E120 E121 E122 E123 E124 E125 E126 E127 E128; do echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/CAPE_eQTL_${e}.vcf.gz >> CAPE_eQTL.txt; done
## Create CAPE_dsQTL
for e in E003 E004 E005 E006 E007 E008 E017 E021 E022 E029 E032 E034 E046 E050 E055 E056 E059 E080 E084 E085 E089 E090 E091 E092 E093 E094 E097 E098 E100 E109 E114 E116 E117 E118 E119 E120 E121 E122 E123 E124 E125 E126 E127 E128; do echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/CAPE_dsQTL_${e}.vcf.gz >> CAPE_dsQTL.txt; done
## Create deltaSVM
for e in E003 E004 E006 E007 E022 E029 E032 E034 E050 E055 E056 E059 E080 E084 E085 E089 E090 E091 E092 E094 E097 E098 E100 E109 E114 E116 E117 E118 E119 E121 E122 E123 E124 E127 E128; do echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/deltaSVM_${e}.vcf.gz >> deltaSVM.txt; done
## Create DeepSEA
for e in E003 E008 E021 E114 E116 E117 E118 E119 E120 E121 E122 E123 E124 E125 E126 E127 E128; do echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/DeepSEA_${e}.vcf.gz >> DeepSEA.txt; done