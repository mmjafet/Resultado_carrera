import mysql.connector
from tabulate import tabulate

# Connect to the database
conn = mysql.connector.connect(
    host="sql10.freesqldatabase.com",
    user="sql10785119",
    password="m5EA4FFDQT",
    database="sql10785119",
    port=3306
)
cursor = conn.cursor()

# Query to join the tables and order by position
query = """
SELECT 
    p.IDParticipant, 
    p.NameParticipant, 
    p.LastName_1, 
    p.LastName_2, 
    p.Category,
    t.StartTime, 
    t.EndTime, 
    t.ElapsedTime, 
    t.Position
FROM 
    Participants p
JOIN 
    TimeResults t ON p.IDParticipant = t.IDParticipant
ORDER BY 
    t.Position ASC, t.ElapsedTime ASC
"""

cursor.execute(query)
results = cursor.fetchall()

# Define column headers for display
headers = ["ID", "Name", "Last Name 1", "Last Name 2", "Category", 
           "Start Time", "End Time", "Elapsed Time", "Position"]

# Display results using tabulate
if results:
    print("\nRace Results (Ordered by Position):")
    print(tabulate(results, headers=headers, tablefmt="grid"))
else:
    print("No race results found.")

# Close connections
cursor.close()
conn.close()