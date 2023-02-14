from pathlib import Path
import os
import shutil

source_dir = Path(r"C:\Users\lucas\IOT\CREMA-D\AudioMP3")
destination_dir = Path(r"C:\Users\lucas\IOT\Mini-CREMA")

files = os.listdir(source_dir)
i = 0
for filepath in source_dir.iterdir():
    if "_ANG_" in filepath.name or "_HAP_" in filepath.name or "_NEU_" in filepath.name:
        i = i+1
        source_path = os.path.join(source_dir, filepath)
        destination_path = os.path.join(destination_dir, filepath)
        shutil.copy2(filepath, destination_dir / filepath.name)

print(f"{i}Files moved successfully")
