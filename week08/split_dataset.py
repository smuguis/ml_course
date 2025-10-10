import os
import shutil
from sklearn.model_selection import train_test_split
from pathlib import Path

src_path = Path(r"D:\development\datasets\Int_ext")
dst_path = Path(r"D:\development\datasets\Int_ext\data")
classes = ['Exterior', 'Interior']

test_size = 0.1
val_size = 0.1
seed = 42

def make_dirs(base_path, class_names):
    for split in ['train', 'val', 'test']:
        for c in class_names:
            (base_path / split / c).mkdir(parents=True, exist_ok=True)

make_dirs(dst_path, classes)

for c in classes:
    files = list((src_path / c).glob('*'))
    train, test = train_test_split(files, test_size=test_size, random_state=seed)
    train, val = train_test_split(train, test_size=val_size, random_state=seed)

    for split, data in zip(['train', 'val', 'test'], [train, val, test]):
        for f in data:
            shutil.copy(f, dst_path / split / c / f.name)

print("split Done")