#batch verifies the validity of HTML files across an entire classes lab submission
#then produces a log file displaying errors in files that fail and clean bills
#of health for those which pass
#uses W3C standard as of 2017

import os
import subprocess
from shutil import copyfile
import shutil

def getsubs(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def getfiles(a_dir):
    return [name for name in os.listdir(a_dir)
            if not os.path.isdir(os.path.join(a_dir, name))]

here = os.getcwd()

lab_number = "11"
lab_name = "Lab" + lab_number

log_file = lab_name + "-htmlvdata.txt"
log_path = os.path.join(here, log_file)

if os.path.exists(log_path):
    os.remove(log_path)

lab_folder = os.path.join(here, lab_name)

students = getsubs(lab_folder)
text = ""
for student in students:
    print(student[5:-2])
    current_folder = os.path.join(lab_folder, student)
    current_students_files = getfiles(current_folder)
    log = open(log_path, "a")
    log.write(student[5:-2] +'\n')
    log.close()
    if any(student + "-htmlfiles.txt" in f for f in current_students_files):
        with open(os.path.join(current_folder, student + "-htmlfiles.txt")) as f:
            current_students_html_list = f.readlines()
            current_students_html_list = [x.strip() for x in current_students_html_list]
        for h in current_students_html_list:
            the_call = "java -jar vnu.jar \"" + lab_name + h.replace("\\", "/")[1:] + "\" 2>> " + log_path
            print (the_call)
            subprocess.call(the_call, shell=True)
        log = open(log_path, "a")
        log.write('\n======================================================================\n')
        log.close()
    else:
        log = open(log_path, "a")
        log.write('Student had no htmlfiles .txt file! \n====================================================================== \n')
        log.close()

subprocess.call('pause', shell=True)
