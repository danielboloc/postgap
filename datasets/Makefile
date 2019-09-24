DEST_DIR=~/Escritorio/PROJECTS/postgap_DB/postgap/datasets
DIR_REGEX=~\/Escritorio\/PROJECTS\/postgap_DB\/postgap\/datasets

default: create download process
create: create_dir
download: d_Jeme_ENCODE d_Jeme_FANTOM5 d_CAPE_eQTL d_CAPE_dsQTL d_deltaSVM d_DeepSEA d_DNase1
process: CAPE_eQTL CAPE_dsQTL deltaSVM DeepSEA Jeme_ENCODE Jeme_FANTOM5 DNase1

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