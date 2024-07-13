
import os
from pathlib import Path


while True:
    project_name = input("Enter the Src Folder Name: ")
    if project_name != '':
        break


list_of_files = [
".github/workflows/.gitkeep",
"qachat.py",
"requirements.txt",
"test.ipynb",
"vision.py",
"Dockerfile",
"app.py",
"setup.py",
".env"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
    if not os.path.exists(filepath):
        with open(filepath,"w") as f:
            pass
    
