import os
import zipfile

cwd = os.getcwd()
for f in os.listdir(cwd):
 f_path = os.path.join(cwd, f)
 if os.path.splitext(f)[1] == ".py":
    if len(os.path.splitext(f)[0].replace(" ", "").split("-")) > 1:
        new_name = f.replace(" ", "").split("-")[2:]
        stringname = ""
        for i in range(len(new_name)):
            stringname = stringname + new_name[i]
        print(stringname)
        new_file_path = os.path.join(cwd, stringname)
        os.rename(f_path, new_file_path)
