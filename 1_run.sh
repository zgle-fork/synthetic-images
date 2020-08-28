# Data
## git clone https://github.com/ych2tj/Video-base-pollen-sacs-coutning.git
## git clone https://github.com/ych2tj/Video-base-pollen-sacs-coutning.git

#env
. activate images

rm TrainingImages/*
# python create.py #use default params: Bacgrounds/ + Objects/ = TraingImages

python create.py --annotate=True --groups=True --mutate=True