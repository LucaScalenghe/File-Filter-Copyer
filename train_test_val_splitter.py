import random
import shutil
from pathlib import Path

# set the paths to the original directory and the new directories for the train, test and val sets
original_dir = Path(r"C:\Users\lucas\Desktop\Mini-CREMA")
train_dir = Path(r"C:\Users\lucas\Desktop\Cartel\Mini-CREMA\train")
test_dir = Path(r"C:\Users\lucas\Desktop\Cartel\Mini-CREMA\test")
val_dir = Path(r"C:\Users\lucas\Desktop\Cartel\Mini-CREMA\val")

# set the split ratios for train, test and val sets
train_ratio = 0.7
test_ratio = 0.2
val_ratio = 0.1

# get a list of all the files in the original directory
file_list = list(original_dir.glob("*"))

# shuffle the file list randomly
random.shuffle(file_list)

# calculate the number of files for each set based on the ratios
train_count = int(len(file_list) * train_ratio)
test_count = int(len(file_list) * test_ratio)
val_count = int(len(file_list) * val_ratio)

# create new directories for the train, test and val sets
# train_dir.mkdir(parents=True, exist_ok=True)
# test_dir.mkdir(parents=True, exist_ok=True)
# val_dir.mkdir(parents=True, exist_ok=True)

# copy the files to the new directories based on the set counts
for i, file in enumerate(file_list):
    if i < train_count:
        shutil.copy2(file, train_dir / file.name)
    elif i < train_count + test_count:
        shutil.copy2(file, test_dir / file.name)
    else:
        shutil.copy2(file, val_dir / file.name)

print(f"{i} files have been splitted")