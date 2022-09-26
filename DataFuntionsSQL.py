from multiprocessing.spawn import prepare
from tkinter import SOLID
from unittest import result
import mysql.connector 
from mysql.connector import Error

connection = mysql.connector.connect(host = 'localhost', 
                                                database = 'python_db',
                                                user= 'root', 
                                                password= '123456')

def save_data_to_DDBB(HospitalID,Hospital_name, Bed_count):
    try: 
          cursor = connection.cursor()
          Intesert_query = """INSERT INTO hospital (HospitalID, Hospital_name, Bed_count) 
                                VALUES (%s, %s, %s)"""

          newHospital= (HospitalID,Hospital_name, Bed_count)
          cursor.execute(Intesert_query, newHospital)
          connection.commit()
          print("New hospital inserted successfully into Hospitals table")
          

    except Error as e:
      print("Failed to insert into MySQL table {}".format(e))
    finally:
      if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
#hi fi



def search():
  
  cursor = connection.cursor()
  search_query = "SELECT Hospital_name, Bed_count, d.Doctor_Name, d.Speciality FROM hospital AS h JOIN doctor AS d on d.Hospital_Id = h.HospitalID"
 
  #lookfor = (Doctor_Name, )
  cursor.execute(search_query)
     
  myresult = cursor.fetchall()
  for x in myresult: 
        print(x)

 
def deleteData():
    Doctor_Id = int (input('\nEnter the ID'))
    cursor = connection.cursor()
    delete_query = "DELETE FROM hospital WHERE HospitalID = %s"
    id= (Doctor_Id, )






