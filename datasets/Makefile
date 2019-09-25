DEST_DIR=~/Escritorio/PROJECTS/postgap_DB/postgap/datasets
DIR_REGEX=~\/Escritorio\/PROJECTS\/postgap_DB\/postgap\/datasets

default: create download process
create: create_dir
download: d_Jeme_ENCODE d_Jeme_FANTOM5 d_CAPE_eQTL d_CAPE_dsQTL d_deltaSVM d_DeepSEA d_DNase1
process: CAPE_eQTL CAPE_dsQTL deltaSVM DeepSEA Jeme_ENCODE Jeme_FANTOM5 DNase1 cleanup

create_dir:
	mkdir -p ${DEST_DIR}	
	mkdir -p ${DEST_DIR}/raw
	mkdir -p ${DEST_DIR}/raw/Jeme_ENCODE
	mkdir -p ${DEST_DIR}/raw/Jeme_FANTOM5
	mkdir -p ${DEST_DIR}/raw/CAPE_eQTL
	mkdir -p ${DEST_DIR}/raw/CAPE_dsQTL
	mkdir -p ${DEST_DIR}/raw/deltaSVM
	mkdir -p ${DEST_DIR}/raw/DeepSEA
	mkdir -p ${DEST_DIR}/raw/DNase1

d_Jeme_ENCODE: # seq 1 127
	-cat ./Jeme_ENCODE.txt | xargs -n1 wget -q -N -P ${DEST_DIR}/raw/Jeme_ENCODE/

d_Jeme_FANTOM5: # seq 1 808
	-cat ./Jeme_FANTOM5.txt | xargs -n1 wget -q -N -P ${DEST_DIR}/raw/Jeme_FANTOM5/

d_CAPE_eQTL: # 3 128
	-cat ./CAPE_eQTL.txt | xargs -n1 wget -q -N -P ${DEST_DIR}/raw/CAPE_eQTL/

d_CAPE_dsQTL: # 3 128
	-cat ./CAPE_dsQTL.txt | xargs -n1 wget -q -N -P ${DEST_DIR}/raw/CAPE_dsQTL/

d_deltaSVM: # 3 128
	-cat ./deltaSVM.txt | xargs -n1 wget -q -N -P ${DEST_DIR}/raw/deltaSVM/

d_DeepSEA: # 3 128
	-cat ./DeepSEA.txt | xargs -n1 wget -q -N -P ${DEST_DIR}/raw/DeepSEA/

d_DNase1:
	-cat ./DNase1.txt | xargs -n1 wget -q -N -P ${DEST_DIR}/raw/DNase1/

define process_SNP_file
zcat $(1) \
| awk 'BEGIN{FS="\t";OFS="\t"} FNR>1 {chr=gsub("chr", "", $$1); print chr, $$2-1, $$2, $$6;}' - \
| sort -k1,1 -k2,2n - \
> $(2);
$(call tabix,$(2));
endef

define process_Jeme_file
awk 'BEGIN{FS=","; OFS="\t"}{split($$1,chr,":"); split(chr[2],pos,"-"); split($$2,gene,"$$"); gsub("chr","",chr[1]); print chr[1],pos[1],pos[2],gene[2],$$3;}' $(1) \
| sort -k1,1 -k2,2n - \
> $(2);
$(call tabix,$(2));
endef

define process_DNase1_file
gunzip $(1)
$(call tabix,$(2));
endef

define bgz
bgzip -f $(1)
endef

define tabix
$(call bgz, $(1))
tabix -f -p bed $(1).gz
endef	

.PHONY: CAPE_eQTL CAPE_dsQTL deltaSVM DeepSEA DNase1

CAPE_eQTL:
	$(eval vcf_files := $(wildcard ${DEST_DIR}/raw/CAPE_eQTL/*.vcf.gz))
	$(foreach file, $(vcf_files), $(call process_SNP_file, $(file),$(subst vcf.gz,bed,$(file))))

CAPE_dsQTL:
	$(eval vcf_files := $(wildcard ${DEST_DIR}/raw/CAPE_dsQTL/*.vcf.gz))
	$(foreach file, $(vcf_files), $(call process_SNP_file, $(file),$(subst vcf.gz,bed,$(file))))

deltaSVM:
	$(eval vcf_files := $(wildcard ${DEST_DIR}/raw/deltaSVM/*.vcf.gz))
	$(foreach file, $(vcf_files), $(call process_SNP_file, $(file),$(subst vcf.gz,bed,$(file))))

DeepSEA:		
	$(eval vcf_files := $(wildcard ${DEST_DIR}/raw/DeepSEA/*.vcf.gz))
	$(foreach file, $(vcf_files), $(call process_SNP_file, $(file),$(subst vcf.gz,bed,$(file))))

Jeme_ENCODE:
	$(eval csv_files := $(wildcard ${DEST_DIR}/raw/Jeme_ENCODE/*.csv))
	$(foreach file, $(csv_files), $(call process_Jeme_file, $(file),$(subst csv,bed,$(file))))

Jeme_FANTOM5:
	$(eval csv_files := $(wildcard ${DEST_DIR}/raw/Jeme_FANTOM5/*.csv))
	$(foreach file, $(csv_files), $(call process_Jeme_file, $(file),$(subst csv,bed,$(file))))

DNase1:
	$(eval gz_files := $(wildcard ${DEST_DIR}/raw/DNase1/*.bed.gz))
	$(foreach file, $(gz_files), $(call process_DNase1_file, $(file),$(subst bed.gz,bed,$(file))))	

cleanup: # remove residual files (.csv;.vcf.gz) to liberate space & change name
	find ./ -type f \( -iname \*.vcf.gz -o -iname \*.csv \) -print0 | xargs -0 rm -f
	find ./ -maxdepth 1 -name 'raw' -type d -print0 | xargs -0 -I % mv % ./processed/

files:
	rm ./Jeme_ENCODE.txt ./Jeme_FANTOM5.txt ./CAPE_eQTL.txt ./CAPE_dsQTL.txt ./deltaSVM.txt ./DeepSEA.txt
	@echo "Removed previous preprocessing files ..."
	@echo "Recreating preprocessing files ..."
	@for e in {1..127}; do echo http://yiplab.cse.cuhk.edu.hk/jeme/encoderoadmap_lasso/encoderoadmap_lasso.$${e}.csv >> Jeme_ENCODE.txt; done
	@for e in {1..808}; do echo http://yiplab.cse.cuhk.edu.hk/jeme/fantom5_lasso/fantom5_lasso.$${e}.csv >> Jeme_FANTOM5.txt; done
	@for e in E003 E004 E005 E006 E007 E008 E017 E021 E022 E029 E032 E034 E046 E050 E055 E056 E059 E080 E084 E085 E089 E090 E091 E092 E093 E094 E097 E098 E100 E109 E114 E116 E117 E118 E119 E120 E121 E122 E123 E124 E125 E126 E127 E128; do echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/CAPE_eQTL_$${e}.vcf.gz >> CAPE_eQTL.txt; done
	@for e in E003 E004 E005 E006 E007 E008 E017 E021 E022 E029 E032 E034 E046 E050 E055 E056 E059 E080 E084 E085 E089 E090 E091 E092 E093 E094 E097 E098 E100 E109 E114 E116 E117 E118 E119 E120 E121 E122 E123 E124 E125 E126 E127 E128; do echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/CAPE_dsQTL_$${e}.vcf.gz >> CAPE_dsQTL.txt; done
	@for e in E003 E004 E006 E007 E022 E029 E032 E034 E050 E055 E056 E059 E080 E084 E085 E089 E090 E091 E092 E094 E097 E098 E100 E109 E114 E116 E117 E118 E119 E121 E122 E123 E124 E127 E128; do echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/deltaSVM_$${e}.vcf.gz >> deltaSVM.txt; done
	@for e in E003 E008 E021 E114 E116 E117 E118 E119 E120 E121 E122 E123 E124 E125 E126 E127 E128; do echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/DeepSEA_$${e}.vcf.gz >> DeepSEA.txt; done	
	@echo "DONE"

test: pre_test
	mkdir -p ${DEST_DIR}/test
	cat ./test/test.txt | xargs wget -N -P ${DEST_DIR}/test/
	# DNase1 first because it decompresses bed.gz
	$(eval gz_file := $(wildcard ${DEST_DIR}/test/*.bed.gz))
	$(foreach file, $(gz_file), $(call process_DNase1_file, $(file),$(subst bed.gz,bed,$(file))))	
	# CAPE, delta, Deep 
	$(eval vcf_file := $(wildcard ${DEST_DIR}/test/*.vcf.gz))
	$(foreach file, $(vcf_file), $(call process_SNP_file, $(file),$(subst vcf.gz,bed,$(file))))
	# Jeme
	$(eval csv_file := $(wildcard ${DEST_DIR}/test/*.csv))
	$(foreach file, $(csv_file), $(call process_Jeme_file, $(file),$(subst csv,bed,$(file))))

pre_test:
	rm -f ${DEST_DIR}/test/test.txt
	@echo "Removed previous testing file ..."
	@echo "Recreating testing file ..."
	@echo http://yiplab.cse.cuhk.edu.hk/jeme/encoderoadmap_lasso/encoderoadmap_lasso.1.csv > ${DEST_DIR}/test/test.txt
	@echo http://yiplab.cse.cuhk.edu.hk/jeme/fantom5_lasso/fantom5_lasso.1.csv >> ${DEST_DIR}/test/test.txt
	@echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/CAPE_eQTL_E003.vcf.gz >> ${DEST_DIR}/test/test.txt
	@echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/CAPE_dsQTL_E003.vcf.gz >> ${DEST_DIR}/test/test.txt
	@echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/deltaSVM_E003.vcf.gz >> ${DEST_DIR}/test/test.txt
	@echo http://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/DeepSEA_E003.vcf.gz >> ${DEST_DIR}/test/test.txt
	@echo http://ftp.ensembl.org/pub/grch37/current/regulation/homo_sapiens/Peaks/A549/DNase1/homo_sapiens.GRCh37.A549.DNase1.SWEmbl_R0005.peaks.20180925.bed.gz >> ${DEST_DIR}/test/test.txt
	@echo "DONE"


clean_raw:
	rm -rf ${DEST_DIR}/raw/*

clean_all:
	rm -rf ${DEST_DIR}/*

clean_test:
	rm -rf ${DEST_DIR}/test/*