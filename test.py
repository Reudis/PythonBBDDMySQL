
from ast import If
from cgi import print_environ
import DataFuntionsSQL as func

print("¡Welcome to Hospital records system!")
print("1.Create a new record.")
print("2.See all records.")
print("3.update a record.")
print("4.Delete a record.")
options = int(input('\nSelect the options you want to use:'))

if options == 1:
  print("Enter the new record ")
  Hospital = int (input('\nEnter the ID'))
  lastname = str (input('\nEnter your Hospital name'))
  length = int (input('\nEnter the bed count'))
  func.save_data_to_DDBB(Hospital, lastname,length)

if options == 2: 
  print("  HOSPITAL ", '  BED ', '  DOCTOR ' ,' Especiality ')
  func.search()

if options == 3:
  print('')
  
if options == 4:
  print('')


  


  