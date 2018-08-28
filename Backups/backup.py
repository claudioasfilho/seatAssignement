


#removing Front Students
#for Student in allStudents:
#	print("Student {0}".format(Student.sNumber))

#	if Student.frontSeat == "X":
#		frontSeats.append(Student)
#		print("Front Seat Student {0}".format(Student.sNumber))
#		allStudents.remove(Student)



def searchAndDelete(character, param, orig, dest):
	itemPosition = []
	TotalNumberofIterations = len(orig)
	for i in range(0, TotalNumberofIterations):
		if param == "gender":
			if orig[i].gender == character:
				itemPosition.append(i)
				dest.append(i)
				#print("Gender {0}".format(dest[i].sNumber))
		elif param == "grade":
			if orig[i].grade == character:
				itemPosition.append(i)
				dest.append(i)
		elif param == "frontSeat":
			if orig[i].frontSeat == character:
				itemPosition.append(i)
				dest.append(i)
		elif param == "Height":
			if orig[i].Height == character:
				itemPosition.append(i)
				dest.append(i)
	#print itemPosition
	#it deletes frontStudents from allStudents list
	deleted = 0
	for i in itemPosition:
		del orig[i-deleted]
		deleted +=1
	del itemPosition[:]




	
'''
for Student in allStudents:
	
		if Student.Height == "T":
			tallSeats.append(Student)
			allStudents.remove(Student)
			#print("Tall Student {0}".format(Student.sNumber))

for Student in allStudents:
	
		if Student.gender == "M":
			male.append(Student)
			#print("Male Student {0}".format(Student.sNumber))
		else:
			female.append(Student)
			#print("Female Student {0}".format(Student.sNumber))
'''			
			
'''
for Student in frontSeats:
	print("Student in Front Seat {0}".format(Student.sNumber))	
	#print Student.sNumber
'''


tallSeats = []
male = []
female = []
goodGrade=[]
badGrade=[]
tallSeats = []


# Seats 1-12 are Front Seats , Seats 1,2,11,12 - Tall

TotalNumberFrontSeats = len(frontSeats)
print("Number of Students in Front Seat : {0} ".format( TotalNumberFrontSeats ) )


#Removing tall seats from front seats
for Student in frontSeats:
	if Student.Height == "T":
		tallSeats.append(Student)
		frontSeats.remove(Student)
		


NumberTallFrontSeat = len(tallSeats)
print("Number of Tall Students in Front Seat {0}: ".format( NumberTallFrontSeat ) )
NumberFrontSeats = len(frontSeats)
print("Number of Students remaining in Front Seat {0}: ".format( NumberFrontSeats ) )

#Randomize tallSeats 
tallSeats = scrambled(tallSeats)
print("Assign Tall Students on the corner seats in the front")



#Assign Tall Students on the corner seats, if there is more than 4 then puts them back into the main list

i = 0

for Student in tallSeats:
	if (i == 0):
		seatAsgt[1] = Student
		print("Student in Front Seat {0} assigned to Seat 1".format(Student.sNumber))
		tallSeats.remove(Student)
	elif (i == 1):
		seatAsgt[2] = Student
		print("Student in Front Seat {0} assigned to Seat 2".format(Student.sNumber))
		tallSeats.remove(Student)
	elif (i == 2):
		seatAsgt[11] = Student
		print("Student in Front Seat {0} assigned to Seat 11".format(Student.sNumber))
		tallSeats.remove(Student)
	elif (i == 3):
		seatAsgt[12] = Student
		print("Student in Front Seat {0} assigned to Seat 12".format(Student.sNumber))
		tallSeats.remove(Student)
	elif (i > 3):
		frontSeats.append(Student)
		tallSeats.remove(Student)
	
	i += 1
		
'''
#Assign Tall Students on the corner seats, if there is more than 4 then puts them back into the main list
del itemPosition[:]
TotalNumberFrontTallSeats = len(tallSeats)

for i in range(0, TotalNumberFrontTallSeats):
	if (i == 0):
		seatAsgt[1] = tallSeats[i]
		itemPosition.append(i)
		print("Student in Front Seat {0} assigned to Seat 1".format(Student.sNumber))
	elif (i == 1):
		seatAsgt[2] = tallSeats[i]
		itemPosition.append(i)
		print("Student in Front Seat {0} assigned to Seat 2".format(Student.sNumber))
	elif (i == 2):
		seatAsgt[11] = tallSeats[i]
		itemPosition.append(i)
		print("Student in Front Seat {0} assigned to Seat 11".format(Student.sNumber))
	elif (i == 3):
		seatAsgt[12] = tallSeats[i]
		itemPosition.append(i)
		print("Student in Front Seat {0} assigned to Seat 12".format(Student.sNumber))
	elif (i > 3):
		frontSeats.append(tallSeats[i])
		itemPosition.append(i)
'''

'''
if (len(tallSeats)==1):
	seatAsgt[1] = tallSeats[0]
	tallSeats.remove(0)
	
elif (len(tallSeats)==2):
	seatAsgt[1] = tallSeats[0]
	seatAsgt[2] = tallSeats[1]
	tallSeats.remove(0)
	tallSeats.remove(1)
	
elif (len(tallSeats)==3):
	seatAsgt[1] = tallSeats[0]
	seatAsgt[2] = tallSeats[1]
	seatAsgt[11] = tallSeats[2]
	tallSeats.remove(0)
	tallSeats.remove(1)
	tallSeats.remove(2)
	
elif (len(tallSeats)==4):
	seatAsgt[1] = tallSeats[0]
	seatAsgt[2] = tallSeats[1]
	seatAsgt[11] = tallSeats[2]
	seatAsgt[12] = tallSeats[3]
	tallSeats.remove(0)
	tallSeats.remove(1)
	tallSeats.remove(2)
	tallSeats.remove(3)
else:
	seatAsgt[1] = tallSeats[0]
	seatAsgt[2] = tallSeats[1]
	seatAsgt[11] = tallSeats[2]
	seatAsgt[12] = tallSeats[3]
	tallSeats.remove(0)
	tallSeats.remove(1)
	tallSeats.remove(2)
	tallSeats.remove(3)
	i = 0
	for  i in len(tallSeats):
		frontSeats.append(Student)
		tallSeats.remove(i)
'''

NumberTallFrontSeat = len(tallSeats)
print("Remaining of Tall Students in Front Seat {0}: ".format( NumberTallFrontSeat ) )

print("removing Good Students")

for Student in frontSeats:
		if ((Student.grade == "A") or (Student.grade == "B")):
			goodGrade.append(Student)
			print("Good Grade {0}".format(Student.sNumber))
			frontSeats.remove(Student)
			
print("removing Bad Students")
for Student in frontSeats:
			badGrade.append(Student)
			print("Bad Grade {0}".format(Student.sNumber))
			frontSeats.remove(Student)
		
			
NumberFrontSeats = len(frontSeats)
print("Number of Students remaining in Front Seat {0}: ".format( NumberFrontSeats ) )
for Student in frontSeats:
	print Student.sNumber
	
#if (len(tallSeats)>4):
'''
	seatAsgt[1] = tallSeats[0]
	seatAsgt[2] = tallSeats[1]
	seatAsgt[11] = tallSeats[2]
	seatAsgt[12] = tallSeats[3]
'''

# Seats 1,2,11,12,13,14,23,24,25,26,28,30,32,34,35,36 are for Tall
'''
for Student in allStudents:
	print Student.sNumber

scrambledFrontSeats = scrambled(frontSeats)
i = 0

for Student in scrambledFrontSeats:
	print("Seat {0} with Student {1}".format(i+1 , Student.sNumber))
	i += 1
'''


#separating Tall Students from Front List
#Adding tall Students to tallSeats list
for i in range(0, TotalNumberFrontSeats):
	if frontSeats[i].Height == "T":
		itemPosition.append(i)
		tallSeats.append(i)
#print itemPosition
#it deletes frontStudents from allStudents list
deleted = 0
for i in itemPosition:
	#print("Deleting Student {0}".format(frontSeats[i-deleted].sNumber))
	del frontSeats[i-deleted]
	deleted +=1
	
	
	
	
#Separating Front Seat Students
frontSeats = []
TotalNumberStudents = len(allStudents)
print("Total Number of Students :{0} ".format( len(allStudents)) )

itemPosition = []
for i in range(0, TotalNumberStudents):
	if allStudents[i].frontSeat == "X":
		frontSeats.append(allStudents[i])
		itemPosition.append(i)
		
#it deletes frontStudents from allStudents list
deleted = 0
for i in itemPosition:
	#print("Deleting Student {0}".format(allStudents[i-deleted].sNumber))
	del allStudents[i-deleted]
	deleted +=1
#deletes position list for future usage
del itemPosition[:]
#endof Separating Front Seat Students

#male = []
#searchAndDelete("M", "gender", frontSeats, male)
#print male

#for Student in male:
#	print Student.sNumber


for Student in frontSeats:
	print Student.sNumber
	
	
##############
# Feb 18 below
##############

#It creates the Seating Chart and fills up with 36 empty seats

emptyStudent = StudentObj("empty","empty","empty", "0","0","0","0","0","0")

emptyTable = TableObj(emptyStudent, emptyStudent, emptyStudent, emptyStudent)

ClassRoom = ClassRoomObj(emptyTable, emptyTable, emptyTable, emptyTable, emptyTable, emptyTable, emptyTable, emptyTable, emptyTable)


#Separating Students by Behavior
badBehavior = []
okBehavior = []
goodBehavior = []

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


"""
print("Total Number of Bad Behavior Students :{0} ".format(badStuCnt))
printStudentDetail("sNumber", badBehavior)

print("Total Number of Ok Behavior Students :{0} ".format(okStuCnt))
printStudentDetail("sNumber", okBehavior)

print("Total Number of Good Behavior Students :{0} ".format(goodStuCnt))
printStudentDetail("sNumber", goodBehavior)
"""



#print(ClassRoom)

#PrintClassRoom(ClassRoom)



#allStudents = scrambled(allStudents)

#printStudentDetail("sNumber", allStudents)

#for Student in allStudents:
#	print (Student.sNumber)

ClassRoom.Table1.SeatA = allStudents[0]
ClassRoom.Table1.SeatB = allStudents[1]
ClassRoom.Table1.SeatC = allStudents[2]
ClassRoom.Table1.SeatD = allStudents[3]

ClassRoom.Table2.SeatA = allStudents[4]
ClassRoom.Table2.SeatB = allStudents[5]
ClassRoom.Table2.SeatC = allStudents[6]
ClassRoom.Table2.SeatD = allStudents[7]

ClassRoom.Table3.SeatA = allStudents[8]
ClassRoom.Table3.SeatB = allStudents[9]
ClassRoom.Table3.SeatC = allStudents[10]
ClassRoom.Table3.SeatD = allStudents[11]

ClassRoom.Table4.SeatA = allStudents[12]
ClassRoom.Table4.SeatB = allStudents[13]
ClassRoom.Table4.SeatC = allStudents[14]
ClassRoom.Table4.SeatD = allStudents[15]

ClassRoom.Table5.SeatA = allStudents[16]
ClassRoom.Table5.SeatB = allStudents[17]
ClassRoom.Table5.SeatC = allStudents[18]
ClassRoom.Table5.SeatD = allStudents[19]

ClassRoom.Table6.SeatA = allStudents[20]
ClassRoom.Table6.SeatB = allStudents[21]
ClassRoom.Table6.SeatC = allStudents[22]
ClassRoom.Table6.SeatD = allStudents[23]

ClassRoom.Table7.SeatA = allStudents[24]
ClassRoom.Table7.SeatB = allStudents[25]
ClassRoom.Table7.SeatC = allStudents[26]
ClassRoom.Table7.SeatD = allStudents[27]

ClassRoom.Table8.SeatA = allStudents[28]
ClassRoom.Table8.SeatB = allStudents[29]
ClassRoom.Table8.SeatC = allStudents[30]
ClassRoom.Table8.SeatD = allStudents[31]

ClassRoom.Table9.SeatA = allStudents[32]
ClassRoom.Table9.SeatB = allStudents[33]
ClassRoom.Table9.SeatC = allStudents[34]
ClassRoom.Table9.SeatD = allStudents[35]

print(ClassRoom.Table1.SeatA)

'''
	if (badStuCnt>0) & (sA != 'B') & (tCnt == 0):
		Student = badBehavior.pop()
		sA = 'B'
		badStuCnt -=1
		tCnt += 1 #one bad Student per table
		
	else : # (no bad Students) or (Last Student was bad)
					
		if (goodStuCnt>0): #(Still have Good Students)
			Student = goodBehavior.pop()
			sA = 'G'
			goodStuCnt -=1
			tCnt += 1
			
		else : #(Still have Ok Students)
			Student = okBehavior.pop()
			sA = 'O'
			okStuCnt -=1
			tCnt += 1
	'''
	
	
	#more complex implementation
	
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
			Student = okBehavior.pop()
			sA = 'O'
			okStuCnt -=1
			tCnt += 1
			
		if (okStuCnt>0) & (tCnt == 2): #(Still have Ok Students)
			Student = okBehavior.pop()
			sA = 'O'
			okStuCnt -=1
			tCnt += 1
		else:							#(or Good Students)
			Student = goodBehavior.pop()
			sA = 'G'
			goodStuCnt -=1
			tCnt += 1
		if (tCnt == 3):
			if (goodStuCnt>0): #(Still have Good Students)
				Student = goodBehavior.pop()
				sA = 'G'
				goodStuCnt -=1
				tCnt += 1
			else : 							#(or Ok Students)
				Student = okBehavior.pop()
				sA = 'O'
				okStuCnt -=1
				tCnt += 1

############################################################
#Front Students
#Separating Students by Behavior

print("Front")
#printStudentDetail("sNumber", frontSeats)

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


############################################################
#Front Students
#Separating Students by Behavior

print("Front")
#printStudentDetail("sNumber", frontSeats)

for Student in frontSeats:
	if Student.behavior == "3":
		badBehavior.append(Student)
		
for Student in frontSeats:
	if (Student.behavior == "1") or (Student.behavior == "2"):
		goodBehavior.append(Student)


badStuCnt = len(badBehavior)
goodStuCnt = len(goodBehavior)


badBehavior = scrambled(badBehavior)
goodBehavior = scrambled(goodBehavior)
