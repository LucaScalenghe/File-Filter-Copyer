import os
from pathlib import Path
import os
import shutil

original_dir = Path(r"C:\Users\lucas\Desktop\Mini-CREMA")
train_dir = Path(r"C:\Users\lucas\Desktop\Cartel\Mini-CREMA\train")
test_dir = Path(r"C:\Users\lucas\Desktop\Cartel\Mini-CREMA\test")
val_dir = Path(r"C:\Users\lucas\Desktop\Cartel\Mini-CREMA\val")

i_ang = 0
i_hap = 0
i_neu = 0
i_tot = 0
for filepath in original_dir.iterdir():
    if "_ANG_" in filepath.name:
        i_ang = i_ang + 1
    if "_HAP_" in filepath.name:
        i_hap = i_hap + 1
    if "_NEU_" in filepath.name:
        i_neu = i_neu + 1
    
    i_tot = i_tot + 1

print("The original directory has this: ")
print(f"{i_ang/i_tot} of anger clips")
print(f"{i_hap/i_tot} of happy clips")
print(f"{i_neu/i_tot} of neutral clips")

# -----------------------------------------------------------------------------------------------------------
i_ang = 0
i_hap = 0
i_neu = 0
i_tot = 0
for filepath in train_dir.iterdir():
    if "_ANG_" in filepath.name:
        i_ang = i_ang + 1
    if "_HAP_" in filepath.name:
        i_hap = i_hap + 1
    if "_NEU_" in filepath.name:
        i_neu = i_neu + 1
    
    i_tot = i_tot + 1

print("The train directory has this: ")
print(f"{i_ang/i_tot} of anger clips")
print(f"{i_hap/i_tot} of happy clips")
print(f"{i_neu/i_tot} of neutral clips")

# -----------------------------------------------------------------------------------------------------------
i_ang = 0
i_hap = 0
i_neu = 0
i_tot = 0
for filepath in test_dir.iterdir():
    if "_ANG_" in filepath.name:
        i_ang = i_ang + 1
    if "_HAP_" in filepath.name:
        i_hap = i_hap + 1
    if "_NEU_" in filepath.name:
        i_neu = i_neu + 1
    
    i_tot = i_tot + 1

print("The test directory has this: ")
print(f"{i_ang/i_tot} of anger clips")
print(f"{i_hap/i_tot} of happy clips")
print(f"{i_neu/i_tot} of neutral clips")

# -----------------------------------------------------------------------------------------------------------
i_ang = 0
i_hap = 0
i_neu = 0
i_tot = 0
for filepath in val_dir.iterdir():
    if "_ANG_" in filepath.name:
        i_ang = i_ang + 1
    if "_HAP_" in filepath.name:
        i_hap = i_hap + 1
    if "_NEU_" in filepath.name:
        i_neu = i_neu + 1
    
    i_tot = i_tot + 1

print("The validation directory has this: ")
print(f"{i_ang/i_tot} of anger clips")
print(f"{i_hap/i_tot} of happy clips")
print(f"{i_neu/i_tot} of neutral clips")