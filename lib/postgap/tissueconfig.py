# Tissues for the current Functional Annotations
# CAPE_eQTL : example file "CAPE_eQTL_E003.vcf.gz" 
# CAPE_dsQTL : example file "CAPE_dsQTL_E003.vcf.gz" 
# deltaSVM : example file "deltaSVM_E003.vcf.gz" 
# DeepSEA : example file "DeepSEA_E003.vcf.gz" 
# CAPE englobes all 2
#  CAPE
#  	| - CAPE_eQTL
#  	| - CAPE_dsQTL
# Jeme_ENCODE : example file "encoderoadmap_lasso.55.csv" 
# Jeme_FANTOM5 : example file "fantom5_lasso.3.csv"
# DNase1 : example file "homo_sapiens.GRCh37.brain.DNase1.SWEmbl_R0005.peaks.20180925.bed.gz" 
# N_sample : is a mean of all the sub-tissues of a certain tissue  
GTEx_tissues = {
	'Adipose':{
		'Jeme_FANTOM5':[4,606,588,587,586,513,514,515,512,490,489,472,468,442,443,432,433,386,226,133,126,118,119,120],
		'Jeme_ENCODE':[62],
		'N_sample': 525},
	'Adrenal Gland':{
		'CAPE':['E080'],
		'deltaSVM':['E080'],
		'Jeme_ENCODE':[78],
		'N_sample':233},
	'Artery':{
		'Jeme_ENCODE':[63],
		'Jeme_FANTOM5':[72,73,74,609,608,607,518,465,282,229,230,231,195,95,72],
		'DNase1':['Aorta'],
		'N_sample':395},
	'Bladder':{
		'Jeme_FANTOM5':[5 ],
		'N_sample':21},
	'Brain':{
		'CAPE':['E125'],
		'deepSEA':['E125'],
		'Jeme_ENCODE':[79,80,68,69,70,65,66,67,72],
		'Jeme_FANTOM5':[6,804,799,798,797,795,794,793,792,791,790,789,788,787,786,785,642,639,632,
		    571,545,546,547,548,549,550,551,552,553,554,555,556,557,558,532,528,520,519,460,424,311,310,304,198,197,94,36,35,34,33,32,31,30,29,28,27,26,25],
		'DNase1':['astrocyte','astrocyte_ENCSR362MQF','astrocyte_ENCSR362MQF_1','brain','brain_ENCSR189GMC','neuron'],
		'N_sample':168},
	'Breast':{
		'CAPE':['E119'],
		'deltaSVM':['E119'],
		'deepSEA':['E119'],
		'Jeme_FANTOM5':[308,235,131],
		'DNase1':['mammary_epithelial_cell','mammary_epithelial_cell_ENCSR044VTN'],
		'N_sample':396},
	'Cells - Cultured fibroblasts':{
		'CAPE':['E055','E056','E126','E128'],
		'deltaSVM':['E055','E056','E128'],
		'deepSEA':['E126','E128'],
		'Jeme_FANTOM5':[611,610,605,577,533,508,506,504,502,499,481,480,466,461,451,449,425,426,416,417,394,395,396,397,393,391,232,233,222,223,224,225,214,199,196,128,107,103,96,97,80],
		'DNase1':['fibroblast_of_dermis','fibroblast_of_lung','foreskin_fibroblast','foreskin_fibroblast_ENCSR856EKB'],
		'N_sample':483},
	'Cells - EBV-transformed lymphocytes':{
		'CAPE':['E116'],
		'deltaSVM':['E116'],
		'deepSEA':['E116'],
		'N_sample':147},
	'Cervix':{
		'Jeme_FANTOM5':[7 ],
		'N_sample':10},
	'Colon':{
		'Jeme_FANTOM5':[8 ,309],
		'CAPE':['E084'],
		'deltaSVM':['E084'],
		'Jeme_ENCODE':[104,73,74],
		'DNase1':['sigmoid_colon'],
		'N_sample':343},
	'Esophagus':{
		'Jeme_ENCODE':[77],
		'Jeme_FANTOM5':[9 ,200],
		'DNase1':['esophagus'],
		'N_sample':431},
	'Fallopian Tube':{'N_sample':8},
	'Heart': {
		'Jeme_ENCODE':[81,93,102,103],
		'Jeme_FANTOM5':[10,40,669,668,667,621,594,593,592,591,581,574,476,477,478,479,438,439,431,400,401,390,385,307,306,280,281],
		'DNase1':['Left_Ventricle','Right_Atrium','cardiac_muscle_cell','heart','heart_right_ventricle'],
		'N_sample':379},
	'Kidney':{
		'Jeme_ENCODE':[84],
		'Jeme_FANTOM5':[11,39,643,634,535,534,524,523,522,516,205,206,207,208],
		'DNase1':['kidney'],
		'N_sample':73},
	'Liver':{
		'Jeme_ENCODE':[64],
		'Jeme_FANTOM5':[12,660,635,580,573,527,526,517,210],
		'DNase1':['hepatocyte'],
		'N_sample':208},
	'Lung' : {
		'CAPE': ['E017'],
		'Jeme_ENCODE':[94,86],
		'Jeme_FANTOM5':[13,303,202],
		'DNase1':['Lung','lung_ENCSR465WKM'],
		'N_sample':515}, 
	'Minor Salivary Gland':{
		'Jeme_FANTOM5':[652,651,650],
		'N_sample':144},
	'Muscle - Skeletal':{
		'CAPE':['E089','E090','E100','E120','E121'],
		'deltaSVM':['E089','E090','E100','E121'],
		'deepSEA':['E120','E121'],
		'Jeme_ENCODE':[105,106,98,88,87],
		'Jeme_FANTOM5':[17,722,507,503,500,463,428,135,134,99],
		'DNase1':['Psoas_Muscle','myotube','skeletal_muscle_myoblast'],
		'N_sample':706},
	'Nerve - Tibial':{'N_sample':532},
	'Ovary':{
		'CAPE':['E097'],
		'deltaSVM':['E097'],
		'Jeme_ENCODE':[95],
		'Jeme_FANTOM5':[14],
		'DNase1':['Ovary'],
		'N_sample':167},
	'Pancreas':{
		'CAPE':['E098'],
		'deltaSVM':['E098'],
		'Jeme_ENCODE':[96,85],
		'Jeme_FANTOM5':[279,106],
		'DNase1':['Pancreas'],
		'N_sample':305},
	'Pituitary':{
		'Jeme_FANTOM5':[796,544],'N_sample':237},
	'Prostate':{
		'Jeme_FANTOM5':[16,470,469,434,435,110,111],'N_sample':221},
	'Skin':{
		'Jeme_FANTOM5':[620,483,484,236,234,191,125,108],
		'DNase1':['keratinocyte'],
		'N_sample':561},
	'Small Intestine':{
		'Jeme_FANTOM5':[18],
		'Jeme_ENCODE':[75,76,107,83],
		'CAPE':['E085','E109'],
		'deltaSVM':['E085','E109'],
		'DNase1':['Small_Intestine'],
		'N_sample':174},
	'Spleen':{
		'Jeme_ENCODE':[111],
		'Jeme_FANTOM5':[19],
		'DNase1':['Spleen'],
		'N_sample':227},
	'Stomach':{
		'CAPE':['E092','E094'],
		'deltaSVM':['E092','E094'],
		'Jeme_ENCODE':[109,108,92,90],
		'DNase1':['Gastric'],
		'N_sample':324},
	'Testis':{
		'Jeme_FANTOM5':[20,675,659],'N_sample':322},
	'Thyroid':{
		'Jeme_FANTOM5':[22],'N_sample':574},
	'Uterus':{
		'Jeme_FANTOM5':[244],'N_sample':129},
	'Vagina':{
		'Jeme_FANTOM5':[666],'N_sample':141},
	'Whole Blood':{
		'CAPE':['E029','E032','E034','E046','E050','E124'],
		'deltaSVM':['E029','E032','E034','E050','E124'],
		'deepSEA':['E124'],
		'JENCODE':[61,29,30],
		'Jeme_FANTOM5':[629,628,627,624,617,458,457,456,455,421,422,423,412,413,389,383,283,240,241,242,243,129,130,90,91,92],
		'N_sample':670}
}