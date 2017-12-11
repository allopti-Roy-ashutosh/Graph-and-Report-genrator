##########
# First major throw

# the code below was used to create the database that was used in the trial runs
# for the first contacts and studies

import sqlite3
import datetime
import random

# the only proper output that is given and can be utilised is .db
conn = sqlite3.connect("Database.db")
c = conn.cursor()

# Create_Table()

c.execute("CREATE TABLE IF NOT EXISTS course ("
          "name TEXT,"
          "id INTEGER"
          ")")
conn.commit()
print("table course created")

c.execute("CREATE TABLE IF NOT EXISTS stud_det("
          "name TEXT,"
          "id INTEGER,"
          "age INTEGER,"
          "branch TEXT,"
          "degree TEXT"
          ")")
conn.commit()
print("table stud_det created")

c.execute("CREATE TABLE IF NOT EXISTS teach_det ("
          "name TEXT,"
          "id INTEGER,"
          "age INTEGER,"
          "department TEXT,"
          "lectures INTEGER"  # lectures is lectures per week
          ")")
conn.commit()
print("table teach_det created")

# making some seed data
stud_names = ['Aishwarya', 'vedant', 'shivangi', 'ankush', 'rida', 'astha', 'ambar', 'shlok', 'abhik', 'suyash']
teach_names = ['Yash', 'Aishwarya', 'vedant', 'shivangi', 'ankush', 'rida', 'astha', 'ambar', 'shlok', 'abhik']
courses = ['C Programming', 'BEE', 'BME', 'Chemistry', 'Applied Physics', 'BE', 'CFIT', 'Network Analysis',
           'Data Analysis', 'Machine Learning']
branch = ['CSE', 'ETC', 'Meta', 'Chemical', 'Civil', 'Electrical']
degree = ['BE', 'BTech']

# writing code to convert the seed data into actual random generated data
# first filling the courses

Ids = list()
for i in range(10):
	Ids.append(random.randint(112, 217))

IDs_set = set(Ids)
ID_List = list(IDs_set)

diff_sizes = 10 - len(ID_List)

while diff_sizes > 0:
	new_item = (random.randint(112, 217))
	for x in ID_List:
		if new_item == x:
			print("Duplicacy, creating new element")
			new_item = (random.randint(112, 217))
		else:
			ID_List.append(new_item)
			diff_sizes -= 1

print("Duplicacy removed")

for i in range(10):
	c.execute("INSERT INTO course VALUES (?, ?)", (courses[i], ID_List[i]))
	conn.commit()

print("Courses data filled")

# now filling information for techer_det assuming there are 50 teachers
# here as well as below we need to make sure that ID's do not duplicate
# to remove any kind of possibliities that the IDs of students or teacher duplicate
# we will use 7 digits for teacher and 8 digits for students

num_teachers = int(input("Enter the number of teachers in the database:  "))

Ids = list()
for i in range(num_teachers):
	Ids.append(random.randint(1022323, 1233219))

IDs_set = set(Ids)
ID_List = list(IDs_set)

diff_sizes = num_teachers - len(ID_List)

while diff_sizes > 0:
	new_item = (random.randint(1022323, 1933219))
	for x in ID_List:
		if new_item == x:
			print("Duplicacy, creating new element")
			new_item = (random.randint(1022323, 1933219))
		else:
			ID_List.append(new_item)
			diff_sizes -= 1

print("Duplicacy removed")

for i in range(num_teachers):
	x = random.randint(0, 9)
	name = teach_names[0]
	if x == 0:
		name = teach_names[0]
	elif x == 1:
		name = teach_names[1]
	elif x == 2:
		name = teach_names[2]
	elif x == 3:
		name = teach_names[3]
	elif x == 4:
		name = teach_names[4]
	elif x == 5:
		name = teach_names[5]
	elif x == 6:
		name = teach_names[6]
	elif x == 7:
		name = teach_names[7]
	elif x == 8:
		name = teach_names[8]
	elif x == 9:
		name = teach_names[9]

	age = random.randint(29, 60)

	x = random.randint(0, 5)
	b = branch[0]
	if x == 0:
		b = branch[0]
	elif x == 1:
		b = branch[1]
	elif x == 2:
		b = branch[2]
	elif x == 3:
		b = branch[3]
	elif x == 4:
		b = branch[4]
	elif x == 5:
		b = branch[5]
	lect = random.randint(10, 20)
	c.execute("INSERT INTO teach_det VALUES (?, ?, ?, ?, ?)", (name, ID_List[i], age, b, lect))
	conn.commit()

print("Teacher data Filled")

# now inputing data for the students, assuming 500 students

num_studs = int(input("Enter the number of students in the database:  "))

Ids = list()
for i in range(num_studs):
	Ids.append(random.randint(19022323, 29933219))

IDs_set = set(Ids)
ID_List = list(IDs_set)

diff_sizes = num_studs - len(ID_List)

while diff_sizes > 0:
	new_item = (random.randint(19022323, 29933219))
	for x in ID_List:
		if new_item == x:
			print("Duplicacy, creating new element")
			new_item = (random.randint(19022323, 29933219))
		else:
			ID_List.append(new_item)
			diff_sizes -= 1

print("Duplicacy removed")

for i in range(num_studs):
	x = random.randint(0, 9)
	name = stud_names[0]
	if x == 0:
		name = stud_names[0]
	elif x == 1:
		name = stud_names[1]
	elif x == 2:
		name = stud_names[2]
	elif x == 3:
		name = stud_names[3]
	elif x == 4:
		name = stud_names[4]
	elif x == 5:
		name = stud_names[5]
	elif x == 6:
		name = stud_names[6]
	elif x == 7:
		name = stud_names[7]
	elif x == 8:
		name = stud_names[8]
	elif x == 9:
		name = stud_names[9]

	age = random.randint(18, 24)

	y = random.randint(0, 1)
	deg = degree[0]
	if y == 0:
		deg = degree[0]
	elif y == 1:
		deg = degree[1]

	x = random.randint(0, 5)
	b = branch[0]
	if x == 0:
		b = branch[0]
	elif x == 1:
		b = branch[1]
	elif x == 2:
		b = branch[2]
	elif x == 3:
		b = branch[3]
	elif x == 4:
		b = branch[4]
	elif x == 5:
		b = branch[5]
	c.execute("INSERT INTO stud_det VALUES (?, ?, ?, ?, ?)", (name, ID_List[i], age, b, deg))
	conn.commit()

print("Student Data Filled")

print("Not creating table class for now")


c.execute("CREATE TABLE IF NOT EXISTS class("
          "date DATE,"
          "stud_id INTEGER,"
          "teach_id INTEGER,"
          "course_id INTEGER,"
          "branch TEXT,"
          "lect INTEGER,"  # lect is lecture number
          "FOREIGN KEY (stud_id) REFERENCES stud_det(id),"
          "FOREIGN KEY (teach_id) REFERENCES teach_id(id),"
          "FOREIGN KEY (course_id) REFERENCES course(id),"
          "FOREIGN KEY (branch) REFERENCES stud_det(branch)"
          ")")
conn.commit()
print("table class created")

c.close()
conn.close()

####################

#this is the second of the codes that was completely thrown out
#This is a database creator using the peewee library in the python

#this is the test module where things are tested before patching them up
from peewee import *

#here we are creating a sqlite database and connecting to it using peewee

bidb = SqliteDatabase('PeeweeDatabase.db')

class Course_Det(Model):
	course_name = CharField()
	course_id = IntegerField()


class Stud_Det(Model):
	stud_name = CharField()
	stud_id = IntegerField()
	stud_age = IntegerField()
	branch = CharField()
	degree = CharField()
	class Meta:
		database = bidb

class Teacher_Det(Model):
	teach_det = CharField()
	teach_id = IntegerField()
	course_name_teach = ForeignKeyField(Course_Det, related_name = 'Course_Name:Teacher')
	course_id_teach = ForeignKeyField(Course_Det, related_name = 'Course_ID:Teacher')
	teach_age = IntegerField()
	class Meta:
		database = bidb

class Attendance(Model):
	stud_id_attend = ForeignKeyField(Stud_Det, related_name = 'Student_ID:Attendance')
	teacd_id_attend = ForeignKeyField(Teacher_Det, related_name = 'Teacher_ID:Attendance')
	date = DateField()
	course_id_attend = ForeignKeyField(Course_Det, related_name = 'Course_ID:Attendance')
	attendance = BooleanField()
	class Meta:
		database = bidb

print(bidb.get_tables())
for table in bidb.get_tables():
	print(table)

print("The Database has been created, now taking data")
print("Taking data for Courses...")
num_courses = int(input("Enter the number of courses"))
for i in range(num_courses):
	c_name = input("Enter the course name ({0}/{1}):  ".format(i+1, num_courses))
	c_num = int(input("Enter the course ID ({0}/{1}):  ".format(i+1, num_courses)))
	data = Course_Det.create(course_name = c_name, course_id = c_num)


################

# this is the simple code that creates a GUI for the application that simply converts feet input into metres

# this was not a major throw but rather code for future use

# Entry Frame for taking the value of feets
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# Declaring the output in form of label
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Declaring the button
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)


# Declaring the three labes'
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)


for child in mainframe.winfo_children():
	child.grid_configure(padx=5, pady=5)

# the below line actually puts the focus on the feet entry box so that the user wont have to go to the entry box
# and then tap there to access the function
feet_entry.focus()

# the below line actually tells the software that if return key is pressed then to the same thing as calling function
# calculate. NOTE: <Return> is for Mac and use Enter for using on Windows
root.bind('<Return>', calculate)

# to run the thing on a loop
root.mainloop()

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()

#############################


# this is the model that runs the gui of software
from tkinter import *
from tkinter import ttk

def show_graph(*args):
   curr = listbox_graphs.curselection()
   if len(curr) == 1:
      curr2 = int(curr[0])
      graph_choice.set('{0}'.format(graphs_name[curr2]))

# Declaring the basic shit
root = Tk()
root.title("Graph Choice")

mainframe = ttk.Frame(root).grid(column=0, row=0)

# Declaring variables
graph_choice = StringVar()

# Declaring the various Chart available
graphs_name = ('Bar Chart', 'Histogram', 'Line Chart', 'Density Chart', 'Area Chart', 'Scatter Chart', 'Box Chart')
graphs = StringVar(value=graphs_name)

#Declaring the various widgets
graph_label = ttk.Label(mainframe, text="Chose the graph:")
listbox_graphs = Listbox(mainframe, height=3, listvariable=graphs)
graph_label_choice1 = ttk.Label(mainframe, text = "Yur Choice is:")
graph_label_choice2 = ttk.Label(mainframe, textvariable = graph_choice)

#Now grid-ing all the widgets
listbox_graphs.grid(column = 2, row = 1, padx = 5, pady = 5)
graph_label.grid(column=1, row=1, padx = 5, pady = 5)
graph_label_choice1.grid(column = 1, row = 2, padx = 5, pady = 5)
graph_label_choice2.grid(column = 2, row = 2, padx =5, pady = 5)

for i in range(0, len(graphs_name), 2):
   listbox_graphs.itemconfigure(i, background = '#f0f0ff')

#binding
listbox_graphs.bind('<<ListboxSelect>>', show_graph)

root.mainloop()

from tkinter import *
from tkinter import ttk
root = Tk()

# Initialize our country "databases":
#  - the list of country codes (a subset anyway)
#  - a parallel list of country names, in the same order as the country codes
#  - a hash table mapping country code to population<
countrycodes = ('ar', 'au', 'be', 'br', 'ca', 'cn', 'dk', 'fi', 'fr', 'gr', 'in', 'it', 'jp', 'mx', 'nl', 'no', 'es', 'se', 'ch')
countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
        'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
        'Sweden', 'Switzerland')
cnames = StringVar(value=countrynames)
populations = {'ar':41000000, 'au':21179211, 'be':10584534, 'br':185971537, \
        'ca':33148682, 'cn':1323128240, 'dk':5457415, 'fi':5302000, 'fr':64102140, 'gr':11147000, \
        'in':1131043000, 'it':59206382, 'jp':127718000, 'mx':106535000, 'nl':16402414, \
        'no':4738085, 'es':45116894, 'se':9174082, 'ch':7508700}

# Names of the gifts we can send
gifts = { 'card':'Greeting card', 'flowers':'Flowers', 'nastygram':'Nastygram'}

# State variables
gift = StringVar()
sentmsg = StringVar()
statusmsg = StringVar()

# Called when the selection in the listbox changes; figure out
# which country is currently selected, and then lookup its country
# code, and from that, its population.  Update the status message
# with the new population.  As well, clear the message about the
# gift being sent, so it doesn't stick around after we start doing
# other things.
def showPopulation(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        code = countrycodes[idx]
        name = countrynames[idx]
        popn = populations[code]
        statusmsg.set("The population of {0} ({1}) is {2}".format(name, code, popn))
    sentmsg.set('')

# Called when the user double clicks an item in the listbox, presses
# the "Send Gift" button, or presses the Return key.  In case the selected
# item is scrolled out of view, make sure it is visible.
#
# Figure out which country is selected, which gift is selected with the
# radiobuttons, "send the gift", and provide feedback that it was sent.
def sendGift(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = countrynames[idx]
        # Gift sending left as an exercise to the reader
        sentmsg.set("Sent %s to leader of %s" % (gifts[gift.get()], name))

# Create and grid the outer content frame
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# Create the different widgets; note the variables that many
# of them are bound to, as well as the button callback.
# Note we're using the StringVar() 'cnames', constructed from 'countrynames'
lbox = Listbox(c, listvariable=cnames, height=5)
lbl = ttk.Label(c, text="Send to country's leader:")
g1 = ttk.Radiobutton(c, text=gifts['card'], variable=gift, value='card')
g2 = ttk.Radiobutton(c, text=gifts['flowers'], variable=gift, value='flowers')
g3 = ttk.Radiobutton(c, text=gifts['nastygram'], variable=gift, value='nastygram')
send = ttk.Button(c, text='Send Gift', command=sendGift, default='active')
sentlbl = ttk.Label(c, textvariable=sentmsg, anchor='center')
status = ttk.Label(c, textvariable=statusmsg, anchor=W)

# Grid all the widgets
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
lbl.grid(column=1, row=0, padx=10, pady=5)
g1.grid(column=1, row=1, sticky=W, padx=20)
g2.grid(column=1, row=2, sticky=W, padx=20)
g3.grid(column=1, row=3, sticky=W, padx=20)
send.grid(column=2, row=4, sticky=E)
sentlbl.grid(column=1, row=5, columnspan=2, sticky=N, pady=5, padx=5)
status.grid(column=0, row=6, columnspan=2, sticky=(W,E))
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)

# Set event bindings for when the selection in the listbox changes,
# when the user double clicks the list, and when they hit the Return key
lbox.bind('<<ListboxSelect>>', showPopulation)
lbox.bind('<Double-1>', sendGift)
root.bind('<Return>', sendGift)

# Colorize alternating lines of the listbox
for i in range(0,len(countrynames),2):
    lbox.itemconfigure(i, background='#f0f0ff')

# Set the starting state of the interface, including selecting the
# default gift to send, and clearing the messages.  Select the first
# country in the list; because the <<ListboxSelect>> event is only
# generated when the user makes a change, we explicitly call showPopulation.
gift.set('card')
sentmsg.set('')
statusmsg.set('')
lbox.selection_set(0)
showPopulation()

root.mainloop()

# filling the mastersoft data with full of shit

import pymysql.cursors
import random

#Declaring variables

# making some seed data
stud_names = ['Aishwarya', 'vedant', 'shivangi', 'ankush', 'rida', 'astha', 'ambar', 'shlok', 'abhik', 'suyash']
teach_names = ['Yash', 'Aishwarya', 'vedant', 'shivangi', 'ankush', 'rida', 'astha', 'ambar', 'shlok', 'abhik']
courses = ['C Programming', 'BEE', 'BME', 'Chemistry', 'Applied Physics', 'BE', 'CFIT', 'Network Analysis',
           'Data Analysis', 'Machine Learning']
branch = ['CSE', 'ETC', 'Meta', 'Chemical', 'Civil', 'Electrical']
degree = ['BE', 'BTech']

Host = 'localhost'
User = 'root'
Password = 'root'
DB = 'mastersoft'

conn = pymysql.connect(host=Host,
                       user=User,
                       password=Password,
                       db=DB,
                       cursorclass=pymysql.cursors.DictCursor)

"""
stud_id, course_id, date, attendace, teacher_id

INSERT
INTO < table > VALUES(values)

print("filling data for stud_attend")
table = 'stud_attend'

with connection.cursor() as cursor:
	# Create a new record
	sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
	cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| stud_id    | varchar(10) | YES  |     | NULL    |       |
| course_id  | varchar(5)  | YES  |     | NULL    |       |
| date       | date        | YES  |     | NULL    |       |
| attendance | char(1)     | YES  |     | NULL    |       |
| Teacher_id | varchar(10) | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+

"""

table = 'stud_attend'
num_teachers = 200
num_studs = 2000

#For Student IDS
Ids = list()
for i in range(num_studs):
	Ids.append(random.randint(19022323, 29933219))
IDs_set = set(Ids)
S_ID_List = list(IDs_set)
diff_sizes = num_studs - len(S_ID_List)
while diff_sizes > 0:
	new_item = (random.randint(19022323, 29933219))
	for x in ID_List:
		if new_item == x:
			print("Duplicacy, creating new element")
			new_item = (random.randint(19022323, 29933219))
		else:
			S_ID_List.append(new_item)
			diff_sizes -= 1
print("Duplicacy removed")

#For course IDS
cid_list =[10009,22341,33123,66345,22546,75553,22342,56235,67298,98263]

for i in range(200):
	#this is to say that we have a record of 200 hundred classes
	stud_id = 



#For teacher IDS

T_Ids = list()
for i in range(num_teachers):
	Ids.append(random.randint(1022323, 1233219))

IDs_set = set(T_Ids)
T_ID_List = list(IDs_set)

diff_sizes = num_teachers - len(T_ID_List)

while diff_sizes > 0:
	new_item = (random.randint(1022323, 1933219))
	for x in T_ID_List:
		if new_item == x:
			print("Duplicacy, creating new element")
			new_item = (random.randint(1022323, 1933219))
		else:
			T_ID_List.append(new_item)
			diff_sizes -= 1

print("Duplicacy removed in teacher IDS")

#For Student IDS
Ids = list()
for i in range(num_studs):
	Ids.append(random.randint(19022323, 29933219))

IDs_set = set(Ids)
S_ID_List = list(IDs_set)

diff_sizes = num_studs - len(S_ID_List)

while diff_sizes > 0:
	new_item = (random.randint(19022323, 29933219))
	for x in ID_List:
		if new_item == x:
			print("Duplicacy, creating new element")
			new_item = (random.randint(19022323, 29933219))
		else:
			S_ID_List.append(new_item)
			diff_sizes -= 1

print("Duplicacy removed")

for i in range
with conn.cursor() as c:
	sql = 'INSERT INTO {0} VALUES ({1},{2},{3},{4},{5})'.format(table, s_id, c_id, date, att, t_id)
	c.execute(sql)

import sqlite3
import datetime
import random

# the only proper output that is given and can be utilised is .db
conn = sqlite3.connect("Database.db")
c = conn.cursor()

# Create_Table()

c.execute("CREATE TABLE IF NOT EXISTS course ("
          "name TEXT,"
          "id INTEGER"
          ")")
conn.commit()
print("table course created")

c.execute("CREATE TABLE IF NOT EXISTS stud_det("
          "name TEXT,"
          "id INTEGER,"
          "age INTEGER,"
          "branch TEXT,"
          "degree TEXT"
          ")")
conn.commit()
print("table stud_det created")

c.execute("CREATE TABLE IF NOT EXISTS teach_det ("
          "name TEXT,"
          "id INTEGER,"
          "age INTEGER,"
          "department TEXT,"
          "lectures INTEGER"  # lectures is lectures per week
          ")")
conn.commit()
print("table teach_det created")

# making some seed data
stud_names = ['Aishwarya', 'vedant', 'shivangi', 'ankush', 'rida', 'astha', 'ambar', 'shlok', 'abhik', 'suyash']
teach_names = ['Yash', 'Aishwarya', 'vedant', 'shivangi', 'ankush', 'rida', 'astha', 'ambar', 'shlok', 'abhik']
courses = ['C Programming', 'BEE', 'BME', 'Chemistry', 'Applied Physics', 'BE', 'CFIT', 'Network Analysis',
           'Data Analysis', 'Machine Learning']
branch = ['CSE', 'ETC', 'Meta', 'Chemical', 'Civil', 'Electrical']
degree = ['BE', 'BTech']

# writing code to convert the seed data into actual random generated data
# first filling the courses

Ids = list()
for i in range(10):
	Ids.append(random.randint(112, 217))

IDs_set = set(Ids)
ID_List = list(IDs_set)

diff_sizes = 10 - len(ID_List)

while diff_sizes > 0:
	new_item = (random.randint(112, 217))
	for x in ID_List:
		if new_item == x:
			print("Duplicacy, creating new element")
			new_item = (random.randint(112, 217))
		else:
			ID_List.append(new_item)
			diff_sizes -= 1

print("Duplicacy removed")

for i in range(10):
	c.execute("INSERT INTO course VALUES (?, ?)", (courses[i], ID_List[i]))
	conn.commit()

print("Courses data filled")

# now filling information for techer_det assuming there are 50 teachers
# here as well as below we need to make sure that ID's do not duplicate
# to remove any kind of possibliities that the IDs of students or teacher duplicate
# we will use 7 digits for teacher and 8 digits for students

num_teachers = int(input("Enter the number of teachers in the database:  "))

Ids = list()
for i in range(num_teachers):
	Ids.append(random.randint(1022323, 1233219))

IDs_set = set(Ids)
ID_List = list(IDs_set)

diff_sizes = num_teachers - len(ID_List)

while diff_sizes > 0:
	new_item = (random.randint(1022323, 1933219))
	for x in ID_List:
		if new_item == x:
			print("Duplicacy, creating new element")
			new_item = (random.randint(1022323, 1933219))
		else:
			ID_List.append(new_item)
			diff_sizes -= 1

print("Duplicacy removed")

for i in range(num_teachers):
	x = random.randint(0, 9)
	name = teach_names[0]
	if x == 0:
		name = teach_names[0]
	elif x == 1:
		name = teach_names[1]
	elif x == 2:
		name = teach_names[2]
	elif x == 3:
		name = teach_names[3]
	elif x == 4:
		name = teach_names[4]
	elif x == 5:
		name = teach_names[5]
	elif x == 6:
		name = teach_names[6]
	elif x == 7:
		name = teach_names[7]
	elif x == 8:
		name = teach_names[8]
	elif x == 9:
		name = teach_names[9]

	age = random.randint(29, 60)

	x = random.randint(0, 5)
	b = branch[0]
	if x == 0:
		b = branch[0]
	elif x == 1:
		b = branch[1]
	elif x == 2:
		b = branch[2]
	elif x == 3:
		b = branch[3]
	elif x == 4:
		b = branch[4]
	elif x == 5:
		b = branch[5]
	lect = random.randint(10, 20)
	c.execute("INSERT INTO teach_det VALUES (?, ?, ?, ?, ?)", (name, ID_List[i], age, b, lect))
	conn.commit()

print("Teacher data Filled")

# now inputing data for the students, assuming 500 students

num_studs = int(input("Enter the number of students in the database:  "))

Ids = list()
for i in range(num_studs):
	Ids.append(random.randint(19022323, 29933219))

IDs_set = set(Ids)
ID_List = list(IDs_set)

diff_sizes = num_studs - len(ID_List)

while diff_sizes > 0:
	new_item = (random.randint(19022323, 29933219))
	for x in ID_List:
		if new_item == x:
			print("Duplicacy, creating new element")
			new_item = (random.randint(19022323, 29933219))
		else:
			ID_List.append(new_item)
			diff_sizes -= 1

print("Duplicacy removed")

for i in range(num_studs):
	x = random.randint(0, 9)
	name = stud_names[0]
	if x == 0:
		name = stud_names[0]
	elif x == 1:
		name = stud_names[1]
	elif x == 2:
		name = stud_names[2]
	elif x == 3:
		name = stud_names[3]
	elif x == 4:
		name = stud_names[4]
	elif x == 5:
		name = stud_names[5]
	elif x == 6:
		name = stud_names[6]
	elif x == 7:
		name = stud_names[7]
	elif x == 8:
		name = stud_names[8]
	elif x == 9:
		name = stud_names[9]

	age = random.randint(18, 24)

	y = random.randint(0, 1)
	deg = degree[0]
	if y == 0:
		deg = degree[0]
	elif y == 1:
		deg = degree[1]

	x = random.randint(0, 5)
	b = branch[0]
	if x == 0:
		b = branch[0]
	elif x == 1:
		b = branch[1]
	elif x == 2:
		b = branch[2]
	elif x == 3:
		b = branch[3]
	elif x == 4:
		b = branch[4]
	elif x == 5:
		b = branch[5]
	c.execute("INSERT INTO stud_det VALUES (?, ?, ?, ?, ?)", (name, ID_List[i], age, b, deg))
	conn.commit()

print("Student Data Filled")

print("Not creating table class for now")

c.execute("CREATE TABLE IF NOT EXISTS class("
          "date DATE,"
          "stud_id INTEGER,"
          "teach_id INTEGER,"
          "course_id INTEGER,"
          "branch TEXT,"
          "lect INTEGER,"  # lect is lecture number
          "FOREIGN KEY (stud_id) REFERENCES stud_det(id),"
          "FOREIGN KEY (teach_id) REFERENCES teach_id(id),"
          "FOREIGN KEY (course_id) REFERENCES course(id),"
          "FOREIGN KEY (branch) REFERENCES stud_det(branch)"
          ")")
conn.commit()
print("table class created")

c.close()
conn.close()

import pymysql.cursors
import random
import datetime

Host = 'localhost'
User = 'root'
Password = 'root'
DB = 'mastersoft'

conn = pymysql.connect(host=Host,
                       user=User,
                       password=Password,
                       db=DB,
                       cursorclass=pymysql.cursors.DictCursor)

#first doing for the table stud_info
branch = ['CSE', 'ETC', 'Meta', 'Chemical', 'Civil', 'Electrical']
stud_names = ['Aishwarya', 'vedant', 'shivangi', 'ankush', 'rida', 'astha', 'ambar', 'shlok', 'abhik', 'suyash']
degree = ['BE', 'BTech']
table = 'class'

lect = 1

for i in range(200):
	#this is to say that there are 200 classes we have record of

	x = random.randint(0, 5)
	b = branch[0]
	if x == 0:
		b = branch[0]
	elif x == 1:
		b = branch[1]
	elif x == 2:
		b = branch[2]
	elif x == 3:
		b = branch[3]
	elif x == 4:
		b = branch[4]
	elif x == 5:
		b = branch[5]

	d = datetime.date.today()

	t_id = random.randint(123456789, 987654321)

	lect = random.randint(1,11)

	for j in range(60):
		#this is to say that there are 60 students in each class

		s_id = random.randint(1234567890,9876543210)
		y = random.randint(0,1)
		At = 'A'
		if y == 1:
			At = 'P'
		else:
			At = 'A'
		with conn.cursor() as c:
			sql = "INSERT INTO {0} VALUES ('{1}','{2}','{3}','{4}','{5}','{6}')".format(table, b, lect, str(d), t_id, s_id, At)
			print(sql)
			c.execute(sql)

		conn.commit()

conn.close()
'''

'''

Following is the code that is currently in implementation

##########__________########________#########
Code in the GUI application

from tkinter import *
from tkinter import ttk
import DataFiles as dfiles

import  Plotter as pltr

def plot_two(*args):

	def lbox1_bind(*args):
		global columns
		curr1 = list_var1.curselection()
		if len(curr1) == 1:
			curr2 = int(curr1[0])
			columns[0] = list_columns[curr2]
			column1.set(columns[0])

	def lbox2_bind(*args):
		global columns
		curr1 = list_var2.curselection()
		if len(curr1) == 1:
			curr2 = int(curr1[0])
			columns[1] = list_columns[curr2]
			column2.set(columns[1])

	#Declaring the variables
	global table_choice
	column1 = StringVar()
	column2 = StringVar()

	# Declaring the list of columns
	list_columns = dfiles.columns(connection_det[1], table_choice)
	list_col_use = StringVar(value=list_columns)

	# making the labels
	label_plot_two = ttk.Label(mainframe, text="For this chart you require two variables")
	label_var1 = ttk.Label(mainframe, text="Independent Variable:")  # this is x
	label_var2 = ttk.Label(mainframe, text="Dependent Variable:")  # this is y
	label_var1_conf = ttk.Label(mainframe, text = "Use X - Axis Variable:")
	label_var2_conf = ttk.Label(mainframe, text="Use Y - Axis Variable:")
	label_x = ttk.Label(mainframe, textvariable = column1)
	label_y = ttk.Label(mainframe, textvariable = column2)
	label_title = ttk.Label(mainframe, text = "Title of Chart:")

	# Declarig the two List box
	list_var1 = Listbox(mainframe, height=3, width=30, listvariable=list_col_use)
	list_var2 = Listbox(mainframe, height=3, width=30, listvariable=list_col_use)

	#Declaring Entrybox for title
	title_string = StringVar()
	title_entry = ttk.Entry(mainframe, width = 30, textvariable = title_string)

	# Now grid-ing the things
	label_plot_two.grid(column=2, row=8, padx=5, pady=5)
	label_var1.grid(column=1, row=9, padx=5, pady=5)
	list_var1.grid(column=2, row=9, padx=5, pady=5)
	label_var1_conf.grid(column = 1, row = 10, padx = 5, pady = 5)
	label_x.grid(column = 2, row = 10, padx = 5, pady = 5)

	label_var2.grid(column=1, row=11, padx=5, pady=5)
	list_var2.grid(column=2, row=11, padx=5, pady=5)
	label_var2_conf.grid(column=1, row=12, padx=5, pady=5)
	label_y.grid(column = 2, row = 12, padx =5, pady =5)

	label_title.grid(column = 1, row = 13, padx =5, pady =5)
	title_entry.grid(column = 2, row = 13, padx = 5, pady = 5)

	for i in range(0, len(list_columns), 2):
		list_var1.itemconfigure(i, background='#f0f0ff')
		list_var2.itemconfigure(i, background = '#f0f0ff')

	list_var1.bind('<<ListboxSelect>>', lbox1_bind)
	list_var2.bind('<<ListboxSelect>>', lbox2_bind)

	def plot_final(*args):
		global graph_chosen, table_choice
		title_string = str(title_entry.get())
		pltr.Graphs(graph = graph_chosen, connection= connection_det[1], column_1= columns[0],
		            column_2=columns[1], table= table_choice, title= title_string)

	#now declaring the buttons
	plot = ttk.Button(mainframe, text = "Plot", command = plot_final)
	plot.grid(column = 3, row = 13, padx = 5, pady = 5)

def plot_one(*args):

	def lbox_bind(*args):
		global columns
		curr1 = list_var.curselection()
		if len(curr1) == 1:
			curr2 = int(curr1[0])
			columns[0] = list_columns[curr2]
			column.set(columns[0])

	global table_choice
	column = StringVar()

	# Declaring the list of columns
	list_columns = dfiles.columns(connection_det[1], table_choice)
	list_col_use = StringVar(value=list_columns)

	#Declaring the labels
	label_plot_one = ttk.Label(mainframe, text="For this chart you require one variable")
	label_var = ttk.Label(mainframe, text="Variable:")  # this is y
	label_var_conf = ttk.Label(mainframe, text="Use Axis Variable:")
	label_y = ttk.Label(mainframe, textvariable=column)
	label_title = ttk.Label(mainframe, text="Title of Chart:")

	# Declarig the List box
	list_var = Listbox(mainframe, height=3, width=30, listvariable=list_col_use)

	# Declaring Entrybox for title
	title_string = StringVar()
	title_entry = ttk.Entry(mainframe, width=30, textvariable=title_string)

	#Grid-ing the things
	label_plot_one.grid(column = 2, row = 8, padx = 5, pady = 5)
	label_var.grid(column = 1, row = 9, padx = 5, pady = 5)
	list_var.grid(column = 2, row = 9, padx = 5, pady = 5)
	label_var_conf.grid(column = 1, row = 10, padx =5, pady =5)
	label_y.grid(column = 2, row = 10, padx =5, pady =5)
	label_title.grid(column = 1, row = 11, padx = 5, pady = 5)
	title_entry.grid(column = 2, row = 11, padx = 5, pady =5)

	for i in range(0, len(list_columns), 2):
		list_var.itemconfigure(i, background='#f0f0ff')

	list_var.bind('<<ListboxSelect>>', lbox_bind)

	def plot_final(*args):
		global graph_chosen, table_choice
		title_string = str(title_entry.get())
		pltr.Graphs(graph=graph_chosen, connection=connection_det[1], column_1=columns[0], table=table_choice, title= title_string)

	# now declaring the buttons
	plot = ttk.Button(mainframe, text="Plot", command=plot_final)
	plot.grid(column=3, row=11, padx=5, pady=5)

def plot(*args, num_vars):
	# Here appending is done at the positon 3
	if num_vars == 1:
		plot_one()
	else:
		plot_two()


def graph_choser(*args):

	# Bar chart[0], scatter chart[5], line chart[2], area chart[4] -> Each require 2 values for the plotting
	# Histogram[1], boxplot[6], density chart[3] -> Each require 1 value for plotting

	def show_graph(*args):
		global number_of_variables, graph_chosen
		curr1 = listbox_graphs.curselection()
		if len(curr1) == 1:
			curr2 = int(curr1[0])
			graph_choice.set('{0}'.format(graphs_name[curr2]))
			graph_chosen = graphs_name[curr2]
			if curr2 ==1 or curr2 == 6 or curr2 == 3:
				number_of_variables = 1
			else:
				number_of_variables = 2

	# Declaring variables
	graphs_name = ('Bar Chart', 'Histogram', 'Line Chart', 'Density Chart', 'Area Chart', 'Scatter Chart', 'Box Chart')
	graphs = StringVar(value=graphs_name)
	graph_choice = StringVar()

	#declaring table_choice to use in global later
	number_of_variables = 0

	# Declaring the labels
	graph_label = ttk.Label(mainframe, text="Chose the graph:")
	label_gchoice1 = ttk.Label(mainframe, text="Use graph:")
	label_gchoice2 = ttk.Label(mainframe, textvariable=graph_choice)
	# Declaring the listbox
	listbox_graphs = Listbox(mainframe, height=3, width=30, listvariable=graphs)
	# grid-ing them all
	listbox_graphs.grid(column=2, row=6, padx=5, pady=5)
	graph_label.grid(column=1, row=6, padx=5, pady=5)
	label_gchoice1.grid(column=1, row=7, padx=5, pady=5)
	label_gchoice2.grid(column=2, row=7, padx=5, pady=5)

	for i in range(0, len(graphs_name), 2):
		listbox_graphs.itemconfigure(i, background='#f0f0ff')

	# binding the things
	listbox_graphs.bind('<<ListboxSelect>>', show_graph)

	def plot_connector(*args):
		global number_of_variables
		plot(num_vars=number_of_variables)

	# Declaring the button
	button_proceed = ttk.Button(mainframe, text="Proceed", command=plot_connector)
	button_proceed.grid(column=3, row=7, padx=5, pady=5)

def tables_choser(*args, conn):

	def show_tables(*args):
		global table_choice
		curr1 = listbox_tables.curselection()
		if len(curr1) == 1:
			curr2 = int(curr1[0])
			t_choice = tables_avail[curr2]
			table_choice = t_choice
			t_choice_str.set('{0}'.format(t_choice))

	# Declaring the variables
	tables_avail = dfiles.table_choice(conn)
	tables_use = StringVar(value=tables_avail)
	# Declaring a variable which will ease the depth problem
	t_choice = tables_avail[0]

	#Declaring the table_choice here, and will later put the global in the functon
	global table_choice
	table_choice = t_choice

	t_choice_str = StringVar()
	# Declaring the labels
	label_table = ttk.Label(mainframe, text="Tables Present:")
	# Delaring the list box
	listbox_tables = Listbox(mainframe, height=3, width=30, listvariable=tables_use)
	# grid-ing the objects
	label_table.grid(column=1, row=5, padx=5, pady=5)
	listbox_tables.grid(column=2, row=5, padx=5, pady=5)
	# Declaring to get alternate colouring in listbox
	for i in range(0, len(tables_avail), 2):
		listbox_tables.itemconfigure(i, background='#f0f0ff')

	# binding that thing
	listbox_tables.bind('<<ListboxSelect>>', show_tables)

	def graph_choser_connector(*args):
		graph_choser()

	# Declaring the button later to do things
	button_confirm = ttk.Button(mainframe, text="Confirm", command=graph_choser_connector)
	button_confirm.grid(column=3, row=5, padx=5, pady=5)


def connector(*args):
	Host = str(host.get())
	User = str(user.get())
	Password = str(password.get())
	DB = str(database.get())
	x = []
	x = dfiles.connector2(Host= Host, User=User, Password=Password, DB=DB)
	if x[0] == 1:
		success.set('Success')
		# appended at index 1
		connection_det.append(x[1])
		tables_choser(conn=connection_det[1])
	elif x[0] == 0:
		success.set('Failure')


# Declaring other variables
number_of_variables = 0
connection_det = list()
connection_det.append('Something')
# thus at index 1 we have the connection
table_choice = None
graph_chosen = None
columns = ['not_none', 'not_none']

#this is the problem area we are unable to declare root properly
root = Tk()
root.title("Report Maker")
#problem solved see the comment in Plotter

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

# now declaring the variables that will be taken as input
host = StringVar()
user = StringVar()
password = StringVar()
database = StringVar()
success = StringVar()

# Declaring the entry points for the information
host_entry = ttk.Entry(mainframe, width=30, textvariable=host)
user_entry = ttk.Entry(mainframe, width=30, textvariable=user)
pass_entry = ttk.Entry(mainframe, width=30, textvariable=password)
db_entry = ttk.Entry(mainframe, width=30, textvariable=database)

# Declaring the button going to link to the connector module
button_connect = ttk.Button(mainframe, text="Connect", command=connector)

# Declaring the labels
label_success = ttk.Label(mainframe, textvariable=success)
label_hname = ttk.Label(mainframe, text="Hostname:")
label_user = ttk.Label(mainframe, text="User:")
label_pass = ttk.Label(mainframe, text="Password:")
label_db = ttk.Label(mainframe, text="Database:")

# grid-ing all the widgets
label_hname.grid(column=1, row=1, padx=5, pady=5)
host_entry.grid(column=2, row=1, padx=5, pady=5)
user_entry.grid(column=2, row=2, padx=5, pady=5)
label_user.grid(column=1, row=2, padx=5, pady=5)
pass_entry.grid(column=2, row=3, padx=5, pady=5)
label_pass.grid(column=1, row=3, padx=5, pady=5)
db_entry.grid(column=2, row=4, padx=5, pady=5)
label_db.grid(column=1, row=4, padx=5, pady=5)
button_connect.grid(column=3, row=2, padx=5, pady=5)
label_success.grid(column=3, row=3, padx=5, pady=5)

root.mainloop()

##########__________########________#########

Following is the code in DataFiles.py

# To connect to the MySQL server on the terminal:
# enter the su or use sudo
# /usr/local/mysql/bin/mysql -u root -p
# This will prompt to ask the password


import pymysql.cursors

import pandas as pd

def connector2(Host, User, Password, DB):
	try:
		conn = pymysql.connect(host=Host,
		                       user=User,
	                          password=Password,
	                          db=DB,
	                          cursorclass=pymysql.cursors.DictCursor)
		return [1,conn]
	except pymysql.Error as e:
		return [0, 0]

def table_choice(conn):
	ut_df = pd.read_sql_query("SHOW TABLES;", conn)
	table_list = list(ut_df['Tables_in_mastersoft'])
	return table_list

def columns(conn, table):
	ut_df = pd.read_sql_query("SELECT * FROM {0}".format(table), conn)
	columns_list = list(ut_df.columns.values)
	return columns_list

def double_selector(conn, table, col1, col2):
	df = pd.read_sql_query("SELECT {0}, {1} FROM {2}".format(col1, col2, table), conn)
	return df

def single_selector(conn, table, column):
	df = pd.read_sql_query("SELECT {0} FROM {1}".format(column, table), conn)
	return df

##########__________########________#########

Following is the code in Plotter.py 

#without using this code it was giving problems like
# http://stackoverflow.com/questions/32019556/matplotlib-crashing-tkinter-application
import matplotlib
matplotlib.use("TkAgg")
#This ^ is a god code, due to this things are working now

from ggplot import ggplot, geom_bar, geom_histogram, geom_density, geom_area, geom_line
from ggplot import aes, geom_abline, geom_hline, geom_vline
from ggplot import geom_point, theme_bw, theme_gray, theme_xkcd
from ggplot import labs, geom_boxplot

import DataFiles as dfile

class Graphs():
	def __init__(self, graph=None, connection=None, column_1 = None, column_2 = None, table = None, title = None):
		if graph == 'Bar Chart': #2
			self.bar_chart(connection, column_1, column_2, table, title)
		elif graph == 'Line Chart': #2
			self.line_chart(connection, column_1, column_2, table, title)
		elif graph == 'Area Chart':  # 2
			self.area_chart(connection, column_1, column_2, table, title)
		elif graph == 'Scatter Chart':  # 2
			self.point_chart(connection, column_1, column_2, table, title)
		elif graph == 'Density Chart': #1
			self.density_chart(connection, column_1, table, title)
		elif graph == 'Histogram':  # 1
			self.hist_chart(connection, column_1, table, title)
		elif graph == 'Box Chart': #1
			self.boxplot(connection, column_1, table, title)
		else:
			raise ValueError("The given argument to graph does not exist")

	def bar_chart(self, conn, column1, column2, table_chosen, title):
		# since this is a bar graph only two columns will be there

		data_df = dfile.double_selector(conn = conn, table= table_chosen, col1 = column1, col2 = column2)

		bar_plot = ggplot(aes(x=column1, weight=column2), data=data_df) + geom_bar() + labs(title=title)
		print(bar_plot)

	def line_chart(self, conn, column1, column2, table_chosen, title):

		data_df = dfile.double_selector(conn=conn, table=table_chosen, col1=column1, col2=column2)

		line_plot = ggplot(aes(y=column2, x=column1), data=data_df) + geom_line() + theme_gray() + labs(title=title)
		print(line_plot)

	def area_chart(self, conn, column1 , column2, table_chosen, title):

		data_df = dfile.double_selector(conn=conn, table=table_chosen, col1=column1, col2=column2)

		ymin = float(input("Enter the minimum value that should be plotted:  "))
		ymax = float(input("Enter the maximum value that should be plotted:  "))

		area_plot = ggplot(aes(x=column2, ymin=ymin, ymax=ymax), data=data_df) + geom_area() + theme_gray() + labs(
			title=title)
		print(area_plot)

	def point_chart(self, conn, column1, column2, table_chosen, title):

		data_df = dfile.double_selector(conn=conn, table=table_chosen, col1=column1, col2=column2)

		point_plot = ggplot(aes(x=column1, y=column2), data=data_df) + geom_point() + theme_gray() + labs(title=title)
		print(point_plot)

	def hist_chart(self, conn, column, table_chosen, title):

		data_df = dfile.single_selector(conn = conn, table = table_chosen, column = column)

		hist_plot = ggplot(aes(x=column), data=data_df) + geom_histogram() + theme_gray() + labs(title=title)
		print(hist_plot)

	def density_chart(self, conn, column, table_chosen, title):

		data_df = dfile.single_selector(conn=conn, table=table_chosen, column=column)

		density_plot = ggplot(aes(x=column), data=data_df) + geom_density() + theme_gray() + labs(title=title)
		print(density_plot)

	def boxplot(self, conn, column, table_chosen, title):

		data_df = dfile.single_selector(conn=conn, table=table_chosen, column=column)

		box_plot = ggplot(aes(x=column), data=data_df) + geom_boxplot() + theme_gray() + labs(title=title)
		print(box_plot)


##########__________########________#########

'''
