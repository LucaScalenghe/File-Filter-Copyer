import os
from pathlib import Path
import shutil
import random

train_dir = Path(r"C:\Users\lucas\Desktop\ciao\train")

i_ang = 0
ang_file_list = []
i_hap = 0
hap_file_list = []
i_neu = 0
neu_file_list = []
i_tot = 0

for filepath in train_dir.iterdir():
    if "_ANG_" in filepath.name:
        i_ang = i_ang + 1
        ang_file_list.append(filepath)
    if "_HAP_" in filepath.name:
        i_hap = i_hap + 1
        hap_file_list.append(filepath)
    if "_NEU_" in filepath.name:
        i_neu = i_neu + 1
        neu_file_list.append(filepath)
    
    i_tot = i_tot + 1

print("The train directory has this: ")
print(f"{i_ang/i_tot} of anger clips, total of {i_ang} clips")
print(f"{i_hap/i_tot} of happy clips, total of {i_hap} clips")
print(f"{i_neu/i_tot} of neutral clips, total of {i_neu} clips")
print("")




num_samples_needed = max(i_ang, i_neu, i_hap)
print(num_samples_needed)

emotion_file_list = [hap_file_list, ang_file_list, neu_file_list]

for emo_list in emotion_file_list:
    if(len(emo_list) < num_samples_needed):
        random.shuffle(emo_list)
        x = 0
        for i in range(num_samples_needed - len(emo_list)):
            new_name = "copy" + emo_list[i].name
            shutil.copy2(emo_list[i], train_dir / new_name)
            print(new_name)
            x = x + 1
        print(x)



print("Now you have the oversampled category")
i_ang = 0
ang_file_list = []
i_hap = 0
hap_file_list = []
i_neu = 0
neu_file_list = []
i_tot = 0

for filepath in train_dir.iterdir():
    if "_ANG_" in filepath.name:
        i_ang = i_ang + 1
        ang_file_list.append(filepath)
    if "_HAP_" in filepath.name:
        i_hap = i_hap + 1
        hap_file_list.append(filepath)
    if "_NEU_" in filepath.name:
        i_neu = i_neu + 1
        neu_file_list.append(filepath)
    
    i_tot = i_tot + 1

print("The train directory has this: ")
print(f"{i_ang/i_tot} of anger clips, total of {i_ang} clips")
print(f"{i_hap/i_tot} of happy clips, total of {i_hap} clips")
print(f"{i_neu/i_tot} of neutral clips, total of {i_neu} clips")
print("")
