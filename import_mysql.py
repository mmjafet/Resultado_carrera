import mysql.connector

conn = mysql.connector.connect(
    host="sql10.freesqldatabase.com",
    user="sql10785119",
    password="m5EA4FFDQT",
    database="sql10785119",
    port=3306
)
cursor = conn.cursor()
# Execute queries here
cursor.close()
conn.close()