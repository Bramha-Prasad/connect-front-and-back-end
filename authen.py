import mysql.connector
from mysql.connector import Error
try:
   p = mysql.connector.connect(host='localhost',
                             database='Poets',
                             user='root',
                             password='Bramha@123')
   
   while True:
      select="select*from Poet_details"
      cursor = p.cursor()
      cursor.execute(select)
      m=cursor.fetchall()
      j=1
      i=1
     
      c=input("Press 1 to SignUp,\n press 2 to login\n press 3 to exit :")
      if(c=='3'):
         break
      if(c=='2'):
          
          u_id=input("Enter User ID: ")
          passwd=input("Enter Password: ")
          for row in m:
              if(u_id==str(row[0])):
                  if(passwd==str(row[1])):
                      print("   hi, "+u_id+",Welcome to the World of Poets:)")
                      print("---------------------------------------------")
                      print("These are the Poets,We have in Our Portal:")
                      for row in m:
                          print(row[0])
                      print("\n")     
                      i=0
                      break
                  
          if(i):
               print("invalid Username or Password")
          
      if(c=='1'):
          u_id=input("Enter User ID: ")
          passwd=input("Enter Password: ")
          
          for row in m:
              if(u_id==str(row[0])):
                 if(passwd==str(row[1])):
                    print("YOU are already Registered ,Please Login ")
                    j=0
                    break
              
             
          if(j):
              insert="insert into Poet_details values(%s,%s)"
              val=(u_id,passwd)
              
              cursor.execute(insert,val)
              
              
          
          p.commit()     
except Error as e :
   print ("Error while connecting to MySQL", e)
finally:
   #closing database connection.
   if(p.is_connected()):
       cursor.close()
       p.close()
       print("MySQL connection is closed")


