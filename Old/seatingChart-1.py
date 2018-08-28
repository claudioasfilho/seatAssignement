from xlrd import open_workbook
import random

class StudentObj(object):
    def __init__(self, sNumber, firstName, lastName, gender, grade, frontSeat,Height):
        self.sNumber = sNumber
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.grade = grade
        self.frontSeat = frontSeat
        self.Height = Height

    def __str__(self):
        return("Student object:\n"
               "  Student Number = {0}\n"
               "  First Name = {1}\n"
               "  Last Name = {2}\n"
               "  Gender = {3}\n"
               "  Grade = {4}\n"
               "  Front Seat = {5} \n"
               "  Height = {6}"
               .format(self.sNumber, self.firstName, self.lastName, self.gender,
                       self.grade, self.frontSeat, self.Height))

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



#It creates the 36 seats
seatAsgt = []

#initializes the seats
for i in range(36):	
	seatAsgt += str(i)

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
	if frontSeats[i].Height == "T":
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

#print frontSeatsTaken

#Deletes Tall Seats for future usage
del tallSeats[:]

for Student in frontSeats:
	print Student.sNumber

# Seats 1-12 are Front Seats , Seats 1,2,11,12 - Already Filled




