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
