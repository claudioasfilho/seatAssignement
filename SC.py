from xlrd import open_workbook
from FunctionsAndClasses import *
import sys, getopt
import os


#it reads the input file
inputfile = sys.argv[1]

if os.path.isfile(inputfile):
    #it Imports the Excel File
    wb = open_workbook(inputfile)
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
else:
    print("{0} does not appear to be a valid file".format(inputfile))
    sys.exit(2)

#for Student in allStudents:
#	printStudentDetail("sNumber", allStudents)

#totalNumberStudents holds the Number of Students in the class
totalNumberStudents = len(allStudents)
print("Total Number of Students In this Class:{0} ".format(totalNumberStudents))

#stuCnt holds the Number of Students not Seated yet
stuCnt = totalNumberStudents

ClassRoom = []
frontSeats = []
behavior3 =[]
behavior2 =[]
behavior1 =[]

for Student in allStudents:
	if Student.frontSeat == "X":
	   frontSeats.append(Student)

allStudents = list(set(allStudents) - set(frontSeats))
frontCnt = len(frontSeats)
totalFront = len(frontSeats)
printLen("Front", frontSeats)
frontSeats = scrambled(frontSeats)

for Student in allStudents:
	if Student.behavior == "3":
	   behavior3.append(Student)

allStudents = list(set(allStudents) - set(behavior3))
behavior3Cnt = len(behavior3)
totalBehavior3 = len(behavior3)
#printLen("behavior3", behavior3)
behavior3 = scrambled(behavior3)

for Student in allStudents:
	if Student.behavior == "2":
	   behavior2.append(Student)

allStudents = list(set(allStudents) - set(behavior2))
behavior2Cnt = len(behavior2)
#printLen("behavior2", behavior2)
behavior2 = scrambled(behavior2)

for Student in allStudents:
	if Student.behavior == "1":
	   behavior1.append(Student)

allStudents = list(set(allStudents) - set(behavior1))
behavior1Cnt = len(behavior1)
#printLen("behavior1", behavior1)
behavior1 = scrambled(behavior1)

behFlag = 0
frontFlag = 0
gradeFlag = 0
badFlag = 'good'
tCnt = 0


#printLen("allStu", allStudents)

#if Front or Bad Behavior 1o assento
	#good 2o assento else ok
	#good 3o assento else ok
	#ok 4o assento else bad



for i in range(0,totalNumberStudents):

	if (frontCnt>0) and (badFlag == 'good') and ((tCnt == 0) or (tCnt == 1)):
		Student = frontSeats.pop()
		behFlag = int(Student.behavior)
		#print(int(Student.behavior))
		if (Student.behavior == '1'):
			badFlag = 'good'
			behFlag = 0
		else :
			badFlag = 'bad'
		frontCnt -=1
		tCnt += 1

	else:#not Front Seaters on first Seat
		if (behavior3Cnt>0) and (badFlag == 'good') and (behFlag != 3) and ( ((tCnt == 0) or (tCnt == 1) or (tCnt == 2)) or (behFlag == 0)):
			Student = behavior3.pop()
			behFlag = 3
			badFlag = 'bad'
			behavior3Cnt -=1
			tCnt += 1
		else : #not Front Seaters or Behavior3 on first Seat
			if(behavior2Cnt>0) and ((badFlag == 'good') )  and (behFlag != 3) and (behFlag != 2) and ( (tCnt == 0) or (tCnt == 1) ):
				Student = behavior2.pop()
				behFlag = 2
				badFlag = 'bad'
				behavior2Cnt -=1
				tCnt += 1
			else:
				if (behavior1Cnt>0) :
					Student = behavior1.pop()
					behFlag = 1
					behavior1Cnt -=1
					tCnt += 1
				else:
					if (behavior2Cnt>0):
						Student = behavior2.pop()
						behFlag = 2
						badFlag = 'bad'
						behavior2Cnt -=1
						tCnt += 1
					else:
						Student = behavior3.pop()
						behFlag = 3
						badFlag = 'bad'
						behavior3Cnt -=1
						tCnt += 1 #more than one bad Student per table

	ClassRoom.append(Student)
	stuCnt +=1
	if (tCnt == 4):
		tCnt = 0
		badFlag = 'good'


print("\n")
i=0
for Student in ClassRoom:

	print ("Name: {0} Behavior:{1} Front:{2} Grade:{3} Gender:{4}" .format(Student.firstName,Student.behavior,Student.frontSeat, Student.grade, Student.gender))
	i +=1
	if (i==4):
		print("\n")
		i=0


#printLen("ClassRoom", ClassRoom)
