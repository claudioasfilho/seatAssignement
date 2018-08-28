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
	   allStudents.remove(Student)
	   

ClassRoom = []
badBehavior = []
okBehavior = []
goodBehavior = []

############################################################
#Front Students
#Separating Students by Behavior

print("Front")
printStudentDetail("firstname", frontSeats)

for Student in frontSeats:
	if Student.behavior == "3":
		badBehavior.append(Student)

for Student in frontSeats:
	if Student.behavior == "2":
		okBehavior.append(Student)
		
for Student in frontSeats:
	if Student.behavior == "1":
		goodBehavior.append(Student)


badStuCnt = len(badBehavior)
okStuCnt = len(okBehavior)
goodStuCnt = len(goodBehavior)


badBehavior = scrambled(badBehavior)
goodBehavior = scrambled(goodBehavior)
okBehavior = scrambled(okBehavior)



sA = 0
tCnt = 0


for i in range(0,len(frontSeats)):
	

	if (badStuCnt>0) & (sA != 'B') & (tCnt == 0):
		Student = badBehavior.pop()
		sA = 'B'
		badStuCnt -=1
		tCnt += 1 #one bad Student per table
		
	else : # (no bad Students) or (Last Student was bad)
					
		if (goodStuCnt>0) & (tCnt == 1): #(Still have Good Students)
			Student = goodBehavior.pop()
			sA = 'G'
			goodStuCnt -=1
			tCnt += 1
		else : 							#(or Ok Students)
			if (okStuCnt>0):
				Student = okBehavior.pop()
				sA = 'O'
				okStuCnt -=1
				tCnt += 1
			else: 
				if (goodStuCnt>0):
					Student = goodBehavior.pop()
					sA = 'G'
					goodStuCnt -=1
					tCnt += 1
				else: 
					Student = badBehavior.pop()
					sA = 'B'
					badStuCnt -=1
					tCnt += 1 #more than one bad Student per table
	

	ClassRoom.append(Student)
	stuCnt +=1
	if (tCnt == 4): tCnt = 0



for Student in ClassRoom:
	print ("Student {0} Grade {1}" .format(Student.sNumber, Student.grade))


#printStudentDetail("sNumber", ClassRoom)

	
#end of Front Students
############################################################

#Separating Students by Behavior

print("All")

for Student in allStudents:
	if Student.behavior == "3":
		badBehavior.append(Student)

for Student in allStudents:
	if Student.behavior == "2":
		okBehavior.append(Student)
		
for Student in allStudents:
	if Student.behavior == "1":
		goodBehavior.append(Student)


badStuCnt = len(badBehavior)
okStuCnt = len(okBehavior)
goodStuCnt = len(goodBehavior)


badBehavior = scrambled(badBehavior)
goodBehavior = scrambled(goodBehavior)
okBehavior = scrambled(okBehavior)




sA = 0
tCnt = 0


for i in range(0,len(allStudents)):
	
	
	if (badStuCnt>0) & (sA != 'B') & (tCnt == 0):
		Student = badBehavior.pop()
		sA = 'B'
		badStuCnt -=1
		tCnt += 1 #one bad Student per table
		
	else : # (no bad Students) or (Last Student was bad)
					
		if (goodStuCnt>0) & (tCnt == 1): #(Still have Good Students)
			Student = goodBehavior.pop()
			sA = 'G'
			goodStuCnt -=1
			tCnt += 1
		else : 							#(or Ok Students)
			if (okStuCnt>0):
				Student = okBehavior.pop()
				sA = 'O'
				okStuCnt -=1
				tCnt += 1
			else: 
				if (goodStuCnt>0):
					Student = goodBehavior.pop()
					sA = 'G'
					goodStuCnt -=1
					tCnt += 1
				else: 
					Student = badBehavior.pop()
					sA = 'B'
					badStuCnt -=1
					tCnt += 1 #more than one bad Student per table
		

	ClassRoom.append(Student)
	stuCnt +=1
	if (tCnt == 4): tCnt = 0


for Student in ClassRoom:
	print ("{0} Behavior {1} Grade {2} Gender {3}" .format(Student.firstName,Student.behavior, Student.grade, Student.gender))
printLen("ClassRoom", ClassRoom)
