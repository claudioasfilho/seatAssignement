from xlrd import open_workbook
import random

class StudentObj(object):
    def __init__(self, sNumber, firstName, lastName, gender, grade, frontSeat,height, behavior):
        self.sNumber = sNumber
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.grade = grade
        self.frontSeat = frontSeat
        self.height = height
        self.behavior = behavior

    def __str__(self):
        return("Student object:\n"
               "  Student Number = {0}\n"
               "  First Name = {1}\n"
               "  Last Name = {2}\n"
               "  Gender = {3}\n"
               "  Grade = {4}\n"
               "  Front Seat = {5} \n"
               "  Height = {6}"
               "  Behavior = {7}"
               .format(self.sNumber, self.firstName, self.lastName, self.gender,
                       self.grade, self.frontSeat, self.height, self.behavior))

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


def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

def printStudentDetail(param, arr):
	for Student in arr:
		if (param == "sNumber"):
			print("Student Number is {0}".format(Student.sNumber))
		elif (param == "firstName"):
			print("Student First Name is {0}".format(Student.firstName))
		elif (param == "lastName"):
			print("Student Last Name is {0}".format(Student.lastName))
		elif (param == "gender"):
			print("Student Gender is {0}".format(Student.gender))
		elif (param == "grade"):
			print("Student Grade is {0}".format(Student.grade))
		elif (param == "frontSeat"):
			print("Student Front Seat Mark is {0}".format(Student.frontSeat))
		elif (param == "height"):
			print("Student Height is {0}".format(Student.height))
		elif (param == "behavior"):
			print("Student Behavior is {0}".format(Student.behavior))



#It creates the 36 empty seats
seatAsgt = []

seatAsgt = [StudentObj("empty", "empty","empty", "0","0","0","0","0" ) for i in range(36)]

printStudentDetail("behavior", seatAsgt)

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


# Seats 1-12 are Front Seats , Seats 1,2,11,12 - Tall


#Separating Tall Students from the front
tallSeats = []
TotalNumberFrontSeats = len(frontSeats)
print("Number of Students in Front Seat : {0} ".format( len(frontSeats) ) )
itemPosition = []
for i in range(0, TotalNumberFrontSeats):
	if frontSeats[i].height == "T":
		#print frontSeats[i].sNumber
		tallSeats.append(frontSeats[i])
		itemPosition.append(i)
#it deletes frontStudents from frontSeats list
deleted = 0
for i in itemPosition:
	#print("Deleting Student {0}".format(frontSeats[i-deleted].sNumber))
	del frontSeats[i-deleted]
	deleted +=1
#deletes position list for future usage
del itemPosition[:]

'''
print ("tallSeats only")
for Student in tallSeats:
	print Student.sNumber
print("Number of Students in tall Seat : {0} ".format( len(tallSeats) ) )
'''
#endof Separating Tall Students from the front

#Assigning Tall seats in the Front
tallSeats = scrambled(tallSeats)


#Assign Tall Students on the corner seats, if there is more than 4 then puts them back into the main list
del itemPosition[:]
i = 0
frontSeatsTaken = 0

for Student in tallSeats:
	if (i == 0):
		seatAsgt[1] = Student
		frontSeatsTaken += 1
		print("Student in Front Seat {0} assigned to Seat 1".format(Student.sNumber))
		print("Student Grade {0} Gender {1}".format(Student.grade, Student.gender))
	elif (i == 1):
		seatAsgt[2] = Student
		frontSeatsTaken += 1
		print("Student in Front Seat {0} assigned to Seat 2".format(Student.sNumber))
		print("Student Grade {0} Gender {1}".format(Student.grade, Student.gender))
	elif (i == 2):
		seatAsgt[11] = Student
		frontSeatsTaken += 1
		print("Student in Front Seat {0} assigned to Seat 11".format(Student.sNumber))
		print("Student Grade {0} Gender {1}".format(Student.grade, Student.gender))
	elif (i == 3):
		seatAsgt[12] = Student
		frontSeatsTaken += 1
		print("Student in Front Seat {0} assigned to Seat 12".format(Student.sNumber))
		print("Student Grade {0} Gender {1}".format(Student.grade, Student.gender))
	elif (i > 3):
		frontSeats.append(Student)
		#print("Student in Front Seat {0} added to the main pool of seats".format(Student.sNumber))
	
	i += 1

#Deletes Tall Seats for future usage
del tallSeats[:]


print ("front Seats Taken: {0} " .format(frontSeatsTaken))
print("Number of Students in Front Seat : {0} ".format( len(frontSeats) ) )



goodGrade = []
badGrade = []

#for Student in frontSeats:
#	print Student.sNumber
	
del itemPosition[:]
i = 0	
for Student in frontSeats:
		if ((Student.grade == "A") or (Student.grade == "B")):
			goodGrade.append(Student)
			itemPosition.append(i)
			#print("Good Grade {0}".format(Student.sNumber))
'''
deleted = 0
for i in itemPosition:
	del frontSeats[i-deleted]
	deleted +=1
#deletes position list for future usage
del itemPosition[:]

print("Number of Students in Front Seat : {0} ".format( len(frontSeats) ) )
'''
print("removing Bad Students")
for Student in frontSeats:
			badGrade.append(Student)
			itemPosition.append(i)
			#print("Bad Grade {0}".format(Student.sNumber))
'''	
deleted = 0
i = 0	
for i in itemPosition:
	del frontSeats[i-deleted]
	deleted +=1
#deletes position list for future usage
del itemPosition[:]
		
print("Number of Students in Front Seat : {0} ".format( len(frontSeats) ) )
'''

#Assigning Tall seats in the Front
badGrade = scrambled(badGrade)
badGradecount = len(badGrade)

goodGrade = scrambled(goodGrade)
goodGradecount = len(goodGrade)

'''
# Seats 1-12 are Front Seats , Seats 1,2,11,12 - Already Filled
#print seatAsgt
Student = seatAsgt.pop(1)
seatAsgt.insert(1, Student)
'''

#start checking from seat 1 on
counter = 1

while (TotalNumberFrontSeats - frontSeatsTaken > 0):

	try:
		#If Student on the other side of the table has a good grade
		if (seatAsgt[counter].grade == "A") or (seatAsgt[counter].grade == "B"):
			#place a Student with a bad Grade in front of it (2 seats+)
			if ( badGradecount > 0): #Have enough badGrade Students?
				Student = badGrade.pop(counter -1)
				seatAsgt.insert(counter+2, Student)
				badGradecount = badGradecount - 1
				print("Student in Front Seat {0} assigned to Seat {1}".format(Student.sNumber, counter+2))
				print("Student Grade {0} Gender {1}".format(Student.grade, Student.gender))
			else:
				Student = goodGrade.pop(counter -1)
				seatAsgt.insert(counter+2, Student)
				goodGradecount -=1
				print("Student in Front Seat {0} assigned to Seat {1}".format(Student.sNumber, counter+2))
				print("Student Grade {0} Gender {1}".format(Student.grade, Student.gender))
		else:
			#place a Student with a Good Grade in front of it (2 seats+)
			
			if ( goodGradecount > 0):#Have enough goodGrade Students?
				Student = goodGrade.pop(counter -1)
				seatAsgt.insert(counter+2, Student)
				goodGradecount -=1
				print("Student in Front Seat {0} assigned to Seat {1}".format(Student.sNumber, counter+2))
				print("Student Grade {0} Gender {1}".format(Student.grade, Student.gender))
				
			else:
				Student = badGrade.pop(counter -1)
				seatAsgt.insert(counter+2, Student)
				badGradecount -=1
				print("Student in Front Seat {0} assigned to Seat {1}".format(Student.sNumber, counter+2))
				print("Student Grade {0} Gender {1}".format(Student.grade, Student.gender))

	except:
		None
		
	counter +=1
	frontSeatsTaken +=1

#print seatAsgt
