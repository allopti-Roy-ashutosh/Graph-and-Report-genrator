# To connect to the MySQL server on the terminal:
# enter the su or use sudo
# /usr/local/mysql/bin/mysql -u root -p
# This will prompt to ask the password


import pymysql.cursors

import pandas as pd
import datetime
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
