
# import sqlite3
# import mysql.connector



# # Connect to MySQL database
# mysql_connection = mysql.connector.connect(host="localhost", user="root", password="", database="cms")
# print("Connection to MySQL DB successful")

# # Fetch data from MySQL database
# mysql_cursor = mysql_connection.cursor()
# mysql_cursor.execute("SELECT * FROM student")
# students = mysql_cursor.fetchall()

# # Create and connect to a new SQLite database
# sqlite_connection = sqlite3.connect("new_cms.db")
# sqlite_cursor = sqlite_connection.cursor()

# # Create the student table in SQLite
# create_student_table = """
# CREATE TABLE IF NOT EXISTS student (
#   s_name TEXT NOT NULL,
#   s_reg TEXT NOT NULL,
#   s_phno TEXT DEFAULT NULL,
#   s_sem TEXT NOT NULL,
#   s_comb TEXT NOT NULL,
#   s_pass TEXT NOT NULL,
#   s_fees TEXT NOT NULL,
#   s_balance INTEGER NOT NULL
# );
# """
# sqlite_cursor.execute(create_student_table)

# # Insert data into the SQLite database
# insert_student_query = """
# INSERT INTO student (s_name, s_reg, s_phno, s_sem, s_comb, s_pass, s_fees, s_balance) 
# VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# """
# for student in students:
#     sqlite_cursor.execute(insert_student_query, student)

# #
# # Commit the changes and close the SQLite connection
# sqlite_connection.commit()
# sqlite_cursor.close()
# sqlite_connection.close()

# # Close the MySQL connection
# mysql_cursor.close()
# mysql_connection.close()
# print("MySQL connection closed")

# print("Data has been successfully transferred to new_cms.db")

# -----------------------------------------------------------------------------------------------------------------

import sqlite3
import mysql.connector

# Connect to MySQL database
mysql_connection = mysql.connector.connect(host="localhost", user="root", password="", database="cms")
print("Connection to MySQL DB successful")


# Fetch data from MySQL database
mysql_cursor = mysql_connection.cursor()
mysql_cursor.execute("SELECT * FROM student")
students = mysql_cursor.fetchall()

# Fetch remaining data from MySQL database
mysql_cursor = mysql_connection.cursor()
mysql_cursor.execute("SELECT * FROM admin")
admins = mysql_cursor.fetchall()

mysql_cursor.execute("SELECT * FROM contact")
contacts = mysql_cursor.fetchall()

mysql_cursor.execute("SELECT * FROM notification")
notifications = mysql_cursor.fetchall()

mysql_cursor.execute("SELECT * FROM tblfiles")
files = mysql_cursor.fetchall()

mysql_cursor.execute("SELECT * FROM teacher")
teachers = mysql_cursor.fetchall()

# Create and connect to a new SQLite database
sqlite_connection = sqlite3.connect("cms.db")
sqlite_cursor = sqlite_connection.cursor()

# Create the student table in SQLite
create_student_table = """
CREATE TABLE IF NOT EXISTS student (
  s_name TEXT NOT NULL,
  s_reg TEXT NOT NULL,
  s_phno TEXT DEFAULT NULL,
  s_sem TEXT NOT NULL,
  s_comb TEXT NOT NULL,
  s_pass TEXT NOT NULL,
  s_fees TEXT NOT NULL,
  s_balance INTEGER NOT NULL
);
"""
sqlite_cursor.execute(create_student_table)


# Create tables in SQLite database
create_admin_table = """
CREATE TABLE IF NOT EXISTS admin (
  a_name TEXT NOT NULL,
  a_pass TEXT NOT NULL
);
"""
sqlite_cursor.execute(create_admin_table)

create_contact_table = """
CREATE TABLE IF NOT EXISTS contact (
  c_name TEXT NOT NULL,
  c_mail TEXT NOT NULL,
  c_msg TEXT NOT NULL
);
"""
sqlite_cursor.execute(create_contact_table)

create_notification_table = """
CREATE TABLE IF NOT EXISTS notification (
  msg TEXT NOT NULL,
  t_name TEXT NOT NULL
);
"""
sqlite_cursor.execute(create_notification_table)

create_files_table = """
CREATE TABLE IF NOT EXISTS tblfiles (
  FileName TEXT NOT NULL,
  Location TEXT NOT NULL
);
"""
sqlite_cursor.execute(create_files_table)

create_teacher_table = """
CREATE TABLE IF NOT EXISTS teacher (
  t_name TEXT NOT NULL,
  t_phno TEXT NOT NULL,
  t_address TEXT NOT NULL,
  t_dept TEXT NOT NULL,
  t_pass TEXT NOT NULL
);
"""
sqlite_cursor.execute(create_teacher_table)

# Insert data into the SQLite database
# # Insert data into the SQLite database
insert_student_query = "INSERT INTO student (s_name, s_reg, s_phno, s_sem, s_comb, s_pass, s_fees, s_balance) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
for student in students:
    sqlite_cursor.execute(insert_student_query, student)

insert_admin_query = "INSERT INTO admin (a_name, a_pass) VALUES (?, ?)"
sqlite_cursor.executemany(insert_admin_query, admins)

insert_contact_query = "INSERT INTO contact (c_name, c_mail, c_msg) VALUES (?, ?, ?)"
sqlite_cursor.executemany(insert_contact_query, contacts)

insert_notification_query = "INSERT INTO notification (msg, t_name) VALUES (?, ?)"
sqlite_cursor.executemany(insert_notification_query, notifications)

insert_files_query = "INSERT INTO tblfiles (FileName, Location) VALUES (?, ?)"
sqlite_cursor.executemany(insert_files_query, files)

insert_teacher_query = "INSERT INTO teacher (t_name, t_phno, t_address, t_dept, t_pass) VALUES (?, ?, ?, ?, ?)"
sqlite_cursor.executemany(insert_teacher_query, teachers)

# Commit the changes and close the SQLite connection
sqlite_connection.commit()
sqlite_cursor.close()
sqlite_connection.close()

# Close the MySQL connection
mysql_cursor.close()
mysql_connection.close()
print("MySQL connection closed")

print("Data has been successfully transferred to new_cms.db")

