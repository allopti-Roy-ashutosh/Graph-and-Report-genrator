#without using this code it was giving problems like
# http://stackoverflow.com/questions/32019556/matplotlib-crashing-tkinter-application
import matplotlib
matplotlib.use("TkAgg")
#This ^ is a god code, due to this things are working now

from ggplot import ggplot, geom_bar, geom_histogram, geom_density, geom_area, geom_line
from ggplot import aes, geom_abline, geom_hline, geom_vline
from ggplot import geom_point, theme_bw, theme_gray, theme_xkcd
from ggplot import labs, geom_boxplot
import datetime
import DataFiles as dfile

class Graphs():
	def __init__(self, graph=None, connection=None, column_1 = None, column_2 = None, table = None, title = None):
		if graph == 'Bar Chart': #2
			now = datetime.datetime.now()
			print(now)
			global a
			a = now
			self.bar_chart(connection, column_1, column_2, table, title)
		elif graph == 'Line Chart': #2
			now = datetime.datetime.now()
			print(now)
			a = now
			self.line_chart(connection, column_1, column_2, table, title)
		elif graph == 'Area Chart':  # 2
			now = datetime.datetime.now()
			print(now)
			a = now
			self.area_chart(connection, column_1, column_2, table, title)
		elif graph == 'Scatter Chart':  # 2
			now = datetime.datetime.now()
			print(now)
			a = now
			self.point_chart(connection, column_1, column_2, table, title)
		elif graph == 'Density Chart': #1
			now = datetime.datetime.now()
			print(now)
			a = now
			self.density_chart(connection, column_1, table, title)
		elif graph == 'Histogram':  # 1
			now = datetime.datetime.now()
			print(now)
			a = now
			self.hist_chart(connection, column_1, table, title)
		elif graph == 'Box Chart': #1
			now = datetime.datetime.now()
			print(now)
			a = now
			self.boxplot(connection, column_1, table, title)
		else:
			raise ValueError("The given argument to graph does not exist")

	def bar_chart(self, conn, column1, column2, table_chosen, title):
		# since this is a bar graph only two columns will be there

		data_df = dfile.double_selector(conn = conn, table= table_chosen, col1 = column1, col2 = column2)

		bar_plot = ggplot(aes(x=column1, weight=column2), data=data_df) + geom_bar() + labs(title=title)
		now = datetime.datetime.now()
		b = now
		print(b)
		print(b-a)
		print(bar_plot)

	def line_chart(self, conn, column1, column2, table_chosen, title):

		data_df = dfile.double_selector(conn=conn, table=table_chosen, col1=column1, col2=column2)

		line_plot = ggplot(aes(y=column2, x=column1), data=data_df) + geom_line() + theme_gray() + labs(title=title)
		now = datetime.datetime.now()
		b = now
		print(b)
		print(b-a)
		print(line_plot)

	def area_chart(self, conn, column1 , column2, table_chosen, title):

		data_df = dfile.double_selector(conn=conn, table=table_chosen, col1=column1, col2=column2)

		ymin = float(input("Enter the minimum value that should be plotted:  "))
		ymax = float(input("Enter the maximum value that should be plotted:  "))

		area_plot = ggplot(aes(x=column2, ymin=ymin, ymax=ymax), data=data_df) + geom_area() + theme_gray() + labs(
			title=title)
		now = datetime.datetime.now()
		b = now
		print(b)
		print(b-a)
		print(area_plot)

	def point_chart(self, conn, column1, column2, table_chosen, title):

		data_df = dfile.double_selector(conn=conn, table=table_chosen, col1=column1, col2=column2)

		point_plot = ggplot(aes(x=column1, y=column2), data=data_df) + geom_point() + theme_gray() + labs(title=title)
		now = datetime.datetime.now()
		b = now
		print(b)
		print(b-a)
		print(point_plot)

	def hist_chart(self, conn, column, table_chosen, title):

		data_df = dfile.single_selector(conn = conn, table = table_chosen, column = column)

		hist_plot = ggplot(aes(x=column), data=data_df) + geom_histogram() + theme_gray() + labs(title=title)
		now = datetime.datetime.now()
		b = now
		print(b)
		print(b-a)
		print(hist_plot)

	def density_chart(self, conn, column, table_chosen, title):

		data_df = dfile.single_selector(conn=conn, table=table_chosen, column=column)

		density_plot = ggplot(aes(x=column), data=data_df) + geom_density() + theme_gray() + labs(title=title)
		now = datetime.datetime.now()
		b = now
		print(b)
		print(b-a)
		print(density_plot)

	def boxplot(self, conn, column, table_chosen, title):

		data_df = dfile.single_selector(conn=conn, table=table_chosen, column=column)

		box_plot = ggplot(aes(x=column), data=data_df) + geom_boxplot() + theme_gray() + labs(title=title)
		now = datetime.datetime.now()
		b = now
		print(b)
		print(b-a)
		print(box_plot)
