from flask import Flask, render_template
import mysql.connector

app = Flask(__name__, static_folder='static')

def get_race_results():
    # Connect to the database
    conn = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10785119",
        password="m5EA4FFDQT",
        database="sql10785119",
        port=3306
    )
    cursor = conn.cursor(dictionary=True)

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

    # Close connections
    cursor.close()
    conn.close()
    
    return results

@app.route('/')
def index():
    results = get_race_results()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)