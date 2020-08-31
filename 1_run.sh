# Data
## git clone https://github.com/ych2tj/Video-base-pollen-sacs-coutning.git
## git clone https://github.com/ych2tj/Video-base-pollen-sacs-coutning.git

#env
# conda env create -f environment.yml #ignore the errors: turicreate is not needed
. activate images 

# python create.py #use default params: Bacgrounds/ + Objects/ = TraingImages
# python create.py --annotate=True -groups=True --mutate=True #-  # default

bg_dir="Data/BG_real/"

obj_dir="Data/PollenDataset/"
out_dir="Out/PollenDataset/"

# obj_dir="Data/PollenDataset_1_img/" #NOTE: / at the end
# out_dir="Out/PollenDataset_1_img/" #NOTE: / at the end

sizes="0.3,0.4,0.5,0.6" #mutate size ratios. NOTE: no spaces
count_per_size=4

mkdir -p $out_dir
rm $out_dir/* -rf

python create.py --backgrounds=$bg_dir --objects=$obj_dir --output=$out_dir --annotate=True -groups=True --mutate=True --sizes=$sizes --count_per_size=$count_per_size