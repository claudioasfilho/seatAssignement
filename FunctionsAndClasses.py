import random


class StudentObj(object):
	#This is the Student Object
    def __init__(self, sNumber, firstName, lastName, gender, grade, frontSeat,height, behavior,fSeat):
        self.sNumber = sNumber
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.grade = grade
        self.frontSeat = frontSeat
        self.height = height
        self.behavior = behavior
        self.fSeat = fSeat

    def __str__(self):
        return("Student object:\n"
               "  Student Number = {0}\n"
               "  First Name = {1}\n"
               "  Last Name = {2}\n"
               "  Gender = {3}\n"
               "  Grade = {4}\n"
               "  Front Seat = {5}\n"
               "  Height = {6}\n"
               "  Behavior = {7}\n"
               "  Former Seat {8}\n"
               .format(self.sNumber, self.firstName, self.lastName, self.gender,
                       self.grade, self.frontSeat, self.height, self.behavior, self.fSeat))

		
"""
Table Setup
	____
 A |	| C
 B |____| D

"""


class TableObj(object):
	#This is the Table Object
	def __init__(self, SeatA, SeatB, SeatC, SeatD):
		self.SeatA = SeatA
		self.SeatB = SeatB
		self.SeatC = SeatC
		self.SeatD = SeatD
		
	def __str__(self):
		return("Table object:\n"
			   "  Seat A = {0}\n"
			   "  Seat B= {1}\n"
			   "  Seat C = {2}\n"
			   "  Seat D = {3}\n"
			   .format(self.SeatA, self.SeatB, self.SeatC, self.SeatD))
		
"""
Classroom Setup
	____		   ____		       ____
 A | 1	| C		A | 2  | C		A | 3  | C 
 B |____| D		B |____| D		B |____| D
 
 	____		   ____		       ____
 A | 4	| C		A | 5  | C		A | 6  | C 
 B |____| D		B |____| D		B |____| D
 
 	____		   ____		       ____
 A | 7	| C		A | 8  | C		A | 9  | C 
 B |____| D		B |____| D		B |____| D

"""
		

class ClassRoomObj(object):
	#This is the School Class Object
	def __init__(self, Table1, Table2, Table3, Table4, Table5, Table6, Table7, Table8, Table9 ):
		self.Table1 = Table1
		self.Table2 = Table2
		self.Table3 = Table3
		self.Table4 = Table4
		self.Table5 = Table5
		self.Table6 = Table6
		self.Table7 = Table7
		self.Table8 = Table8
		self.Table9 = Table9
		
	def __str__(self):
		return("Table object:\n"
			   "  Table 1 = {0}\n"
			   "  Table 2 = {1}\n"
			   "  Table 3 = {2}\n"
			   "  Table 4 = {3}\n"
			   "  Table 5 = {4}\n"
			   "  Table 6 = {5}\n"
			   "  Table 7 = {6}\n"
			   "  Table 8 = {7}\n"
			   "  Table 9 = {8}\n"
			   .format(self.Table1, self.Table2, self.Table3, self.Table4, self.Table5, self.Table6, self.Table7, self.Table8, self.Table9, ))



#To Ramdomize objets in an Array
#usage: tallSeats = scrambled(tallSeats)
def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

def printLen(param, arr):
	print("{0} cnt: {1}".format(param,len(arr)))
	
	
#to print arguments on an array
#usage: printStudentDetail("sNumber", seatAsgt)
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
		elif (param == "fSeat"):
			print("Student Former Seat is {0}".format(Student.fSeat))
		
def PrintClassRoom(ClassRoom):
	print("{0}	| 1  |	{1}	{2}	| 2  |	{3}	{4}	| 3  |	{5}".format(ClassRoom.Table1.SeatA.sNumber, ClassRoom.Table1.SeatC.sNumber, ClassRoom.Table2.SeatA.sNumber, ClassRoom.Table2.SeatC.sNumber, ClassRoom.Table3.SeatA.sNumber, ClassRoom.Table3.SeatC.sNumber))
	print("{0}	|____|	{1}	{2}	|____|	{3}	{4}	|____|	{5}".format(ClassRoom.Table1.SeatB.sNumber, ClassRoom.Table1.SeatD.sNumber, ClassRoom.Table2.SeatB.sNumber, ClassRoom.Table2.SeatD.sNumber, ClassRoom.Table3.SeatB.sNumber, ClassRoom.Table3.SeatD.sNumber))
	print("															")
	print("{0}	| 4  |	{1}	{2}	| 5  |	{3}	{4}	| 6  |	{5}".format(ClassRoom.Table4.SeatA.sNumber, ClassRoom.Table4.SeatC.sNumber, ClassRoom.Table5.SeatA.sNumber, ClassRoom.Table5.SeatC.sNumber, ClassRoom.Table6.SeatA.sNumber, ClassRoom.Table6.SeatC.sNumber))
	print("{0}	|____|	{1}	{2}	|____|	{3}	{4}	|____|	{5}".format(ClassRoom.Table4.SeatB.sNumber, ClassRoom.Table4.SeatD.sNumber, ClassRoom.Table5.SeatB.sNumber, ClassRoom.Table5.SeatD.sNumber, ClassRoom.Table6.SeatB.sNumber, ClassRoom.Table6.SeatD.sNumber))
	print("															")
	print("{0}	| 7  |	{1}	{2}	| 8  |	{3}	{4}	| 9  |	{5}".format(ClassRoom.Table7.SeatA.sNumber, ClassRoom.Table7.SeatC.sNumber, ClassRoom.Table8.SeatA.sNumber, ClassRoom.Table8.SeatC.sNumber, ClassRoom.Table9.SeatA.sNumber, ClassRoom.Table9.SeatC.sNumber))
	print("{0}	|____|	{1}	{2}	|____|	{3}	{4}	|____|	{5}".format(ClassRoom.Table7.SeatB.sNumber, ClassRoom.Table7.SeatD.sNumber, ClassRoom.Table8.SeatB.sNumber, ClassRoom.Table8.SeatD.sNumber, ClassRoom.Table9.SeatB.sNumber, ClassRoom.Table9.SeatD.sNumber))
	print("															")