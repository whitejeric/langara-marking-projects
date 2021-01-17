#E White, Langara College Lab Assistant (Jan 2017)
#deployed within an archive containing unzipped student java coding assignment submissions
#this script finds and reorganizes the contents of each submission to a uniform submission folder structure
#in order to easily compile, execute and inject test cases to each .java file and automatically
#produce a well formatted marking rubric with detailed information on how each program succeeded or
#failed a given test

import os
import subprocess
from shutil import copyfile
import shutil


def getsubs(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def getjava(source_dir, dest_dir):
    for f in os.listdir(source_dir):
        if f.lower().endswith('.java') and not f.startswith('.'): #added !f.startswith('.') march 19th
            if os.path.isfile(os.path.join(dest_dir, f)):
                oldfile = os.path.join(dest_dir, f)
                newfile = os.path.join(source_dir, f)
                if os.path.getctime(oldfile) < os.path.getctime(newfile):
                    os.remove(oldfile)
                    copyfile(newfile, oldfile)
            else:
                copyfile(os.path.join(source_dir, f), os.path.join(dest_dir, f))
        elif os.path.isdir(os.path.join(source_dir, f)):
            getjava(os.path.join(source_dir, f), dest_dir)

#for each folder from get_immediate_subdirectories
students = getsubs('.')
for student in students:
    print(student)
    src = os.path.join('.', student)
    dest = os.path.join(src, 'javasources')
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    getjava(src, dest)
subprocess.call('pause', shell=True)
