import os
import zipfile

cwd = os.getcwd()
for f in os.listdir(cwd):
 f_path = os.path.join(cwd, f)
 if os.path.splitext(f)[1] == ".zip":
    folder_name = os.path.splitext(f)[0].replace(" ", "").split("-")[2]
    print(folder_name)
    new_folder_path = os.path.join(cwd, folder_name)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
    new_zip_file_path = os.path.join(new_folder_path, f)
    os.rename(f_path, new_zip_file_path)
    zippy = zipfile.ZipFile(new_zip_file_path)
    zippy.extractall(new_folder_path)
    zippy.close()
