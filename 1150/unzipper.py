#E White, Langara College Lab Assistant (Jan 2017)
#deployed within a folder containing (hopefully!) uniformly named .zipped student
#submissions this script unzips and creates uniform folder hierarchies in order to
#more easily automate my marking scripts upon them

import zipfile
import os

for f in os.listdir('.'):
    if f.lower().endswith('.zip'):
        Student = f.split('-')
        studentName = Student[2].strip('_')
        if (len(Student) < 6):
            studentNumber = '000000000'
            print(studentName + ' NO SID!')
        else:
            studentNumber = Student[-4].strip('_')
            print(studentName + " " + studentNumber)
        studentFolder = studentName + '-' + studentNumber
        zip_ref = zipfile.ZipFile(os.path.join(os.getcwd(), f), 'r')
        zip_ref.extractall(os.path.join(os.getcwd(), studentFolder))
        zip_ref.close()
