import os
import zipfile

cwd = os.getcwd()
for f in os.listdir(cwd):
    f_path = os.path.join(cwd, f)
    if len(os.path.splitext(f)[0].replace(" ", "").split("-")) > 1 and os.path.splitext(f)[1] != ".py":
        new_name = f.replace(" ", "").split("-")[2:]
        stringname = ""
        for i in range(len(new_name)):
            stringname = stringname + new_name[i]
        print(stringname)
        new_file_path = os.path.join(cwd, stringname)
        os.rename(f_path, new_file_path)

cwd = os.getcwd()
for f in os.listdir(cwd):
 f_path = os.path.join(cwd, f)
 if os.path.splitext(f)[1] != ".py" and "Nov" in f:
    folder_name = os.path.splitext(f)[0].split("Nov")[0]
    print(os.path.splitext(f)[0].split("Nov")[0])
    new_folder_path = os.path.join(cwd, folder_name)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
    new_file_path = os.path.join(new_folder_path, f)
    os.rename(f_path, new_file_path)
