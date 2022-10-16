import mysql.connector

#Connect to MariaDB via .connect method and user the root user 
final_assess = mysql.connector.connect(user = 'root')
print(final_assess)

mycursor = final_assess.cursor()


mycursor.execute("DROP DATABASE IF EXISTS Marketing;")
mycursor.execute("CREATE DATABASE IF NOT EXISTS Marketing;")
mycursor.execute("SHOW DATABASES;")