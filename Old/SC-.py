from xlrd import open_workbook
#from collections import deque
#import random
#import UserDict
from FunctionsAndClasses import *


#it Imports the Excel File
wb = open_workbook('SeatAssignment.xls')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    allStudents = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        Student = StudentObj(*values)
        allStudents.append(Student)


#for Student in allStudents:
#	printStudentDetail("sNumber", allStudents)

#totalNumberStudents holds the Number of Students in the class
totalNumberStudents = len(allStudents)
print("Total Number of Students In this Class:{0} ".format(totalNumberStudents))

#stuCnt holds the Number of Students not Seated yet
stuCnt = totalNumberStudents
frontSeats = []

for Student in allStudents:
	if Student.frontSeat == "X":
	   frontSeats.append(Student)
	   
allStudents = list(set(allStudents) - set(frontSeats))

#print("Total Number of Students In this Class:{0} ".format(len(allStudents)))



ClassRoom = []
badBehavior = []
okBehavior = []
goodBehavior = []
goodGrade = []
badGrade = []


############################################################
#Front Students
#Separating Students by Behavior

print("Front")

#print("Total Number in Front:{0} ".format(len(frontSeats)))
#printStudentDetail("sNumber", frontSeats)

for Student in frontSeats:
	if Student.behavior == "3":
		badBehavior.append(Student)
		
for Student in frontSeats:
	if (Student.behavior == "1") or (Student.behavior == "2"):
		goodBehavior.append(Student)


badStuCnt = len(badBehavior)
goodStuCnt = len(goodBehavior)

#printLen("Good Behavior", goodBehavior)


badBehavior = scrambled(badBehavior)
goodBehavior = scrambled(goodBehavior)


#### Within Good Behavior Students ####
for Student in goodBehavior:
	if (Student.grade == "A") or (Student.grade == "B"):
		goodGrade.append(Student)
	else :
		badGrade.append(Student)
		
badGradeCnt = len(badGrade)
goodGradeCnt = len(goodGrade)

badGrade = scrambled(badGrade)
goodGrade= scrambled(goodGrade)


# BehaviorFlag - 'B' = Bad, 'G' = Good, 'O' = Ok
BehaviorFlag = 0 
#GradeFlag - 'A' = Good, 'F' = Bad
GradeFlag = 0
tCnt = 0


for i in range(0,len(frontSeats)):
	
	#print(str(i))
	if (badStuCnt>0) & (BehaviorFlag != 'B') & (tCnt == 0):
		Student = badBehavior.pop()
		BehaviorFlag = 'B'
		badStuCnt -=1
		tCnt += 1 #one bad Student per table
		
	else : # (no bad Students) or (Last Student was bad)
					
		if (goodGradeCnt>0) & (tCnt == 1): #(Still have Good Students)
			Student = goodGrade.pop()
			BehaviorFlag = 'G'
			GradeFlag = 'A'
			goodGradeCnt -=1
			tCnt += 1
		else : 							#(or Ok Students)
			if (badGradeCnt>0):
				Student = badGrade.pop()
				BehaviorFlag = 'O'
				GradeFlag = 'F'
				badGradeCnt -=1
				tCnt += 1
			else: 
				if (goodGradeCnt>0):
					Student = goodGrade.pop()
					BehaviorFlag = 'G'
					GradeFlag = 'A'
					goodGradeCnt -=1
					tCnt += 1
				else: 
					Student = badBehavior.pop()
					BehaviorFlag = 'B'
					badStuCnt -=1
					tCnt += 1 #more than one bad Student per table
	

	ClassRoom.append(Student)
	stuCnt +=1
	if (tCnt == 4): tCnt = 0

'''

for Student in ClassRoom:
	print ("Student {0} Grade {1}" .format(Student.sNumber, Student.grade))

'''
#printStudentDetail("sNumber", ClassRoom)

	
#end of Front Students
############################################################

#Separating Students by Behavior

print("All")

for Student in allStudents:
	if Student.behavior == "3":
		badBehavior.append(Student)
		
for Student in allStudents:
	if (Student.behavior == "1") or (Student.behavior == "2"):
		goodBehavior.append(Student)


badStuCnt = len(badBehavior)
goodStuCnt = len(goodBehavior)

#printLen("Good Behavior", goodBehavior)


badBehavior = scrambled(badBehavior)
goodBehavior = scrambled(goodBehavior)


#### Within Good Behavior Students ####
for Student in goodBehavior:
	if (Student.grade == "A") or (Student.grade == "B"):
		goodGrade.append(Student)
	else :
		badGrade.append(Student)
		
badGradeCnt = len(badGrade)
goodGradeCnt = len(goodGrade)

badGrade = scrambled(badGrade)
goodGrade= scrambled(goodGrade)


# BehaviorFlag - 'B' = Bad, 'G' = Good, 'O' = Ok
BehaviorFlag = 0 
#GradeFlag - 'A' = Good, 'F' = Bad
GradeFlag = 0
tCnt = 0


for i in range(0,len(allStudents)):
	
	#print(str(i))
	if (badStuCnt>0) & (BehaviorFlag != 'B') & (tCnt == 0):
		Student = badBehavior.pop()
		BehaviorFlag = 'B'
		badStuCnt -=1
		tCnt += 1 #one bad Student per table
		
	else : # (no bad Students) or (Last Student was bad)
					
		if (goodGradeCnt>0) & (tCnt == 1): #(Still have Good Students)
			Student = goodGrade.pop()
			BehaviorFlag = 'G'
			GradeFlag = 'A'
			goodGradeCnt -=1
			tCnt += 1
		else : 							#(or Ok Students)
			if (badGradeCnt>0):
				Student = badGrade.pop()
				BehaviorFlag = 'O'
				GradeFlag = 'F'
				badGradeCnt -=1
				tCnt += 1
			else: 
				if (goodGradeCnt>0):
					Student = goodGrade.pop()
					BehaviorFlag = 'G'
					GradeFlag = 'A'
					goodGradeCnt -=1
					tCnt += 1
				else: 
					Student = badBehavior.pop()
					BehaviorFlag = 'B'
					badStuCnt -=1
					tCnt += 1 #more than one bad Student per table
	

	ClassRoom.append(Student)
	stuCnt +=1
	if (tCnt == 4): tCnt = 0



for Student in ClassRoom:
	print ("{0} Student {1} Grade {2} Gender {3}" .format(Student.firstName,Student.sNumber, Student.grade, Student.gender))
printLen("ClassRoom", ClassRoom)
