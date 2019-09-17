#! /usr/bin/env python

"""

Copyright [1999-2018] EMBL-European Bioinformatics Institute

Licensed under the Apache License, Version 2.0 (the "License")
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

		 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

"""

	Please email comments or questions to the public Ensembl
	developers list at <http://lists.ensembl.org/mailman/listinfo/dev>.

	Questions may also be sent to the Ensembl help desk at
	<http://www.ensembl.org/Help/Contact>.

"""
from postgap.DataModel import Region

TYPE = None
OUTPUT = None
DATABASES_DIR = None
SPECIES = None
DEBUG = True

BLACKLISTED_REGIONS = [
	Region(chrom = '6', start=28477797, end=33448354), # MHC
	Region(chrom = '17', start=44165260, end=44784489) # Dan Wright's inversion
]

EVIDENCE_WEIGHTS = {
	'Regulome': 1,
	'VEP': 1,
	'CAPE_eQTL': 1,
	'CAPE_dsQTL': 1,
	'deltaSVM': 1,
	'DeepSEA': 1,
	'CATO': 1,
	'DNase1': 1,
	'GTEx': 1,
	'Fantom5': 1,
	'DHS': 1,
	'PCHiC': 1,
	'Jeme_ENCODE': 1,
	'Jeme_FANTOM5': 1,
	'GERP':1,
	'Nearest': 1,
	'Diff_Meth': 1,
	'GWAS_Genes': 1
}

GWAS_adaptors = None
Cisreg_adaptors = None
Reg_adaptors = None

GTEx_path = None
SQLite_connection = None
work_directory = "notset"
finemap_gwas_clusters_directory = None

GWAS_PVALUE_CUTOFF = 1e-4

GWAS_SUMMARY_STATS_FILE = None

PERFORM_BAYESIAN = False

ALL_TISSUES=[]
USER_TISSUE = None

source_list=[]

CAPE_eQTL_TISSUES=[]

CAPE_dsQTL_TISSUES=[]

deltaSVM_TISSUES=[]

DeepSEA_TISSUES=[]

DNase1_TISSUES=[]

Jeme_ENCODE_TISSUES=[]

Jeme_FANTOM5_TISSUES=[]

