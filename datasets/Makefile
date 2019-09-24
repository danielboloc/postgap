DEST_DIR=~/Escritorio/PROJECTS/postgap_DB/postgap/datasets
DIR_REGEX=~\/Escritorio\/PROJECTS\/postgap_DB\/postgap\/datasets

default: create download process
create: create_dir
download: d_DNase1 tabix
#process: Jeme_FANTOM5

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
	@for e in $$(seq 1 2); do wget -N -P ${DEST_DIR}/raw/Jeme_ENCODE/ http://yiplab.cse.cuhk.edu.hk/jeme/encoderoadmap_lasso/encoderoadmap_lasso.$${e}.csv; done

d_Jeme_FANTOM5: # seq 1 808
	@for e in $$(seq 1 2); do wget -N -P ${DEST_DIR}/raw/Jeme_FANTOM5/ http://yiplab.cse.cuhk.edu.hk/jeme/fantom5_lasso/fantom5_lasso.$${e}.csv; done

d_CAPE_eQTL: # 3 128
	@for e in $$(seq -f "%03g" 3 4); do wget -N -P ${DEST_DIR}/raw/CAPE_eQTL/ ftp://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/CAPE_eQTL_E$${e}.vcf.gz; done

d_CAPE_dsQTL: # 3 128
	@for e in $$(seq -f "%03g" 3 4); do wget -N -P ${DEST_DIR}/raw/CAPE_dsQTL/ ftp://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/CAPE_dsQTL_E$${e}.vcf.gz; done

d_deltaSVM: # 3 128
	@for e in $$(seq -f "%03g" 3 4); do wget -N -P ${DEST_DIR}/raw/deltaSVM/ ftp://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/deltaSVM_E$${e}.vcf.gz; done

d_DeepSEA: # 3 128
	-for e in $$(seq -f "%03g" 3 4); do wget -N -P ${DEST_DIR}/raw/DeepSEA/ ftp://ftp.ncbi.nlm.nih.gov/pub/snpdelscore/rawdata/DeepSEA_E$${e}.vcf.gz; done

d_DNase1:
	-cat ./DNase1.txt | xargs -n1 wget -q -N -P ${DEST_DIR}/raw/DNase1/

# Jeme_ENCODE:
# 	@for f in $(wildcard ${DEST_DIR}/raw/Jeme_ENCODE/*.csv) ; do \
# 		awk 'BEGIN{FS=","; OFS="\t"}{split($$1,chr,":"); split(chr[2],pos,"-"); split($$2,gene,"$$"); gsub("chr","",chr[1]); print chr[1],pos[1],pos[2],gene[2],$$3;}' $$f | sort -k 1,1 -k2,2n $$f >> $${f%.csv}.bed; done

# Jeme_FANTOM5:
# 	@for f in $(wildcard ${DEST_DIR}/raw/Jeme_FANTOM5/*.csv) ; do \
# 		awk 'BEGIN{FS=","; OFS="\t"}{split($$1,chr,":"); split(chr[2],pos,"-"); split($$2,gene,"$$"); gsub("chr","",chr[1]); print chr[1],pos[1],pos[2],gene[2],$$3;}' $$f | sort -k 1,1 -k2,2n $$f >> $${f%.csv}.bed; done
tabix: bgzip
	$(eval bgz_files:=$(wildcard ${DEST_DIR}/raw/DNase1/*.bed.gz))
	$(foreach file, $(gz_files), tabix -f -p bed $(file);)

bgzip: unzip
	$(eval bed_files:=$(wildcard ${DEST_DIR}/raw/DNase1/*.bed))
	$(foreach file, $(bed_files), bgzip $(file);)

unzip:
	$(eval gz_files:=$(wildcard ${DEST_DIR}/raw/DNase1/*.bed.gz))
	$(foreach file, $(gz_files), gunzip $(file);)


define process_SNP_file
zcat $(1) \
| awk 'BEGIN{FS="\t";OFS="\t"} FNR>1 {chr=gsub("chr", "", $$1); print chr, $$2-1, $$2, $$6;}' - \
| sort -k1,1 -k2,2n - \
> `dirname $(1)`/`basename $(1) | sed -e 's/vcf.gz/bed/'`;
bgzip -f `dirname $(1)`/`basename $(1) | sed -e 's/vcf.gz/bed/'`;
tabix -f -p bed `dirname $(1)`/`basename $(1) | sed -e 's/vcf.gz/bed/'`.gz;
endef

define process_Jeme_file
awk 'BEGIN{FS=","; OFS="\t"}{split($$1,chr,":"); split(chr[2],pos,"-"); split($$2,gene,"$$"); gsub("chr","",chr[1]); print chr[1],pos[1],pos[2],gene[2],$$3;}' $(1) \
| sort -k1,1 -k2,2n - \
> `dirname $(1)`/`basename $(1) | sed -e 's/csv/bed/'`;
bgzip -f `dirname $(1)`/`basename $(1) | sed -e 's/csv/bed/'`;
tabix -f -p bed `dirname $(1)`/`basename $(1) | sed -e 's/csv/bed/'`.gz;
endef

define bgz
bgzip -f $(1)
endef

define tabix
$(call bgz, $(1))
tabix -f -p bed $(1).gz
endef	

.PHONY: CAPE_eQTL CAPE_dsQTL deltaSVM DeepSEA 

CAPE_eQTL:
	$(eval vcf_files := $(wildcard ${DEST_DIR}/raw/CAPE_eQTL/*.vcf.gz))
	$(foreach file, $(vcf_files), $(call process_SNP_file, $(file)))

CAPE_dsQTL:
	$(eval vcf_files := $(wildcard ${DEST_DIR}/raw/CAPE_dsQTL/*.vcf.gz))
	$(foreach file, $(vcf_files), $(call process_SNP_file, $(file)))

deltaSVM:
	$(eval vcf_files := $(wildcard ${DEST_DIR}/raw/deltaSVM/*.vcf.gz))
	$(foreach file, $(vcf_files), $(call process_SNP_file, $(file)))

DeepSEA:		
	$(eval vcf_files := $(wildcard ${DEST_DIR}/raw/DeepSEA/*.vcf.gz))
	$(foreach file, $(vcf_files), $(call process_SNP_file, $(file)))

Jeme_ENCODE:
	$(eval csv_files := $(wildcard ${DEST_DIR}/raw/Jeme_ENCODE/*.csv))
	$(foreach file, $(csv_files), $(call process_Jeme_file, $(file)))

Jeme_FANTOM5:
	$(eval csv_files := $(wildcard ${DEST_DIR}/raw/Jeme_FANTOM5/*.csv))
	$(foreach file, $(csv_files), $(call process_Jeme_file, $(file)))

DNase1:
	$(eval csv_files := $(wildcard ${DEST_DIR}/raw/DNase1/*.bed.gz))	