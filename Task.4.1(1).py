# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3
# Создание таблицы Students
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL PRIMARY KEY,
School_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL);"""
cursor.execute(query)
connection.commit()
connection.close()

import sqlite3
# Наполнение таблицы данными:
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
VALUES
('201', 'Иван', '1'),
('202', 'Петр', '2'),
('203', 'Анастасия', '3'),
('204', 'Игорь', '4');"""
cursor.execute(query)
connection.commit()
connection.close()

import sqlite3
#  Программа по информации:
def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM School WHERE School_Id = ?"
    cursor.execute(query,(school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Error) as error:
    print ('Ошибка в получении данных ', error)


def get_student(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM Students WHERE Student_Id = ?"""
    cursor.execute(query,(student_id,))
    records = cursor.fetchall()
    print ("Данные по студенту:")
    for row in records:
      print ("ID студента:", row[2])
      print ("Имя студента:", row[1])
      print ("Название школы:", get_school_name(row[0]))
      print ("Номер школы:", row[0])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ('Ошибка в получении данных ', error)

get_student(201)
# get_student(202)
# get_student(203)
# get_student(204)