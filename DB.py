import mysql.connector
conn=mysql.connector.connect(user='root',password='Asusfra/12345')
mycursor=conn.cursor()
mycursor.execute('show databases')
mycursor.fetchall()
