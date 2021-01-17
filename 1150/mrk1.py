#E White, Langara College Lab Assistant (Jan 2017)
#compiles and tests all .java files within a single given students submission folder
#allows test cases to be inputted manually and prompts user to assign a grade for each
#program and test case which is then appended to an overview XML containing all students grades
#to populate individual html based markups of their grades for their feedback


import subprocess
import os
import sys
import xml
import xml.etree.cElementTree as ET
from lxml import etree


#inputs: (pathToFiles, pathToXML, pathToLog, student)
prgrmRoot = os.getcwd()
if (len(sys.argv) > 5):
    pathToFiles =  sys.argv[1].replace('\\', '\\\\')
    pathToXML = sys.argv[2].replace('\\', '\\\\')
    pathToLog = sys.argv[3].replace('\\', '\\\\')
    pathToMarked = sys.argv[4].replace('\\', '\\\\')
    student = sys.argv[5]
else:
    print('Missing inputs, ending.')

def comp(fileName):
        subprocess.call('javac ' + fileName, shell=True)


#programName := filename of the .java file in question
#studentName := the name of the student of whose program we are evaluating
#qNum        := the relavent question number from the students assignment
def runOne(programName, studentName, qNum):
    runAgain = 'y'
    while (runAgain != 'n'):
        subprocess.call('java ' + programName, shell=True)
        runAgain = input('\nRun again? (y/n): ')
    checkSrc = input('Check source code? (y/n): ')
    if (checkSrc == 'y'):
        openSrc(programName)
    mark(programName, studentName, qNum)

def compileAll():
    for f in os.listdir('.'):
        if f.lower().endswith('.java'):
            comp(f)

def runAll(studentName):
    i = 1
    for f in os.listdir('.'):
        if f.lower().endswith('.class'):
            prgName = os.path.splitext(f)[0]
            print('\n=========== Problem ' + prgName +' =========')
            runOne(prgName, studentName, i)
            print('____________________________________')
            i = i + 1

def openSrc(programName):
    subprocess.call('notepad ' + programName +'.java', shell=True)

def mark(programName, studentName, qNum):
    global pathToXML
    global pathToFiles
    global student
    tree = ET.parse(pathToXML)
    xmlRoot = tree.getroot()
    comments = input("Comments: ")
    numMark = input("Mark: ")
    foundEntry = False
    for child in xmlRoot.findall('Student'):
        if (child.get('name') == student):
            foundEntry = True
            P = ET.Element("Problem", name=programName)
            ET.SubElement(P, "Mark").text = numMark
            ET.SubElement(P, "Comments").text = comments
            child.append(P)
    if (foundEntry == False):
        newStudent = ET.Element('Student', name=student)
        ET.SubElement(newStudent, "Problem", name=programName)
        ET.SubElement(newStudent[0], "Mark").text = numMark
        ET.SubElement(newStudent[0], "Comments").text = comments
        xmlRoot.append(newStudent)
    tree.write(pathToXML)

def prettyPrintXml(xmlFilePathToPrettyPrint):
    assert xmlFilePathToPrettyPrint is not None
    parser = etree.XMLParser(resolve_entities=False, strip_cdata=False)
    document = etree.parse(xmlFilePathToPrettyPrint, parser)
    document.write(xmlFilePathToPrettyPrint, pretty_print=True, encoding='utf-8')

#os.chdir('py mrk1.py C:\Users\ew\Desktop\marking\Bradley_Wing-100284767\test C:\Users\ew\Desktop\marking\resources\lab2.xml C:\Users\ew\Desktop\marking\resources\log.txt C:\Users\ew\Desktop\marking\resources\marked.txt  BradleyWing')
#os.chdir('py mrk1.py [PATH TO FILES] [PATH TO XML] [PATH TO LOGFILE] [PATH TO MARKED STUDENTS FILE] [STUDENT NAME]')

markFile = open(pathToMarked, 'r')
markedStudents = markFile.read().splitlines()

skipStudent = ''

for students_already_marked in markedStudents:
    if students_already_marked == student:
        skipStudent = input(student + ' has already been marked, skip student? (y/n): ')

if (skipStudent != 'y'):
    os.chdir(pathToFiles)
    compileAll()
    runAll(student)
    markingComplete = input('Marking completed? (y/n): ')
    if (markingComplete == 'n'):
        runAll(student)
        markFile = open(pathToMarked, 'a+')
        markFile.write('\n' + student)
    else:
        markFile = open(pathToMarked, 'a+')
        markFile.write('\n' + student)
    prettyPrintXml(pathToXML)

os.chdir(prgrmRoot)

subprocess.call('pause', shell=True)
subprocess.call('\&cls', shell=True)
