#E White, Langara College Lab Assistant (Jan 2017)
#creates an interface through which to batch mark an entire classes java coding submissions
#if interrupted (by user or poorly written java code) maintains a list of all
#previously marked students in order to avoid having to remark already processed
#submissions

import os
import subprocess
from shutil import copyfile
import shutil


def getsubs(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

#os.chdir('py mrk1.py [PATH TO FILES] [PATH TO XML] [PATH TO LOGFILE] [PATH TO MARKED STUDENTS FILE] [STUDENT NAME]')
here = os.getcwd()

lab_folder = os.path.join(os.pardir, 'lab7')
resource_path = os.path.join(here, 'resources')
path_to_logfile = os.path.join(resource_path, 'log.txt')
path_to_marked_students = os.path.join(resource_path, 'marked.txt')
path_to_xml = os.path.join(resource_path, 'grades.xml')

students = getsubs(lab_folder)

for student in students:
    print(student)
    path_to_student = os.path.join(lab_folder, student)
    path_to_files = os.path.join(path_to_student, 'javasources')
    name = student.split('-')[0]
    the_call = 'py mrk1.py ' + path_to_files + ' ' + path_to_xml + ' ' + path_to_logfile + ' ' + path_to_marked_students + ' ' + name
    subprocess.call(the_call, shell=True)
subprocess.call('pause', shell=True)
