# Data
## git clone https://github.com/ych2tj/Video-base-pollen-sacs-coutning.git
## git clone https://github.com/ych2tj/Video-base-pollen-sacs-coutning.git

#env
conda env create -f environment.yml #ignore the errors: turicreate is not needed
. activate images 

rm TrainingImages/*
# python create.py #use default params: Bacgrounds/ + Objects/ = TraingImages

python create.py --annotate=True --groups=True --mutate=True