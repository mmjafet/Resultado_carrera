from flask import Flask, render_template
import mysql.connector

app = Flask(__name__, static_folder='static')

def get_race_results():
    # Conéctate a la base de datos
    conn = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10786405",
        password="ygewRIuATj",
        database="sql10786405",
        port=3306
    )
    cursor = conn.cursor(dictionary=True)

    # Consulta para obtener resultados
    query = """
    SELECT 
        p.IDParticipant, 
        p.NameParticipant, 
        p.LastName_1, 
        p.LastName_2, 
        p.Category,
        t.StartTime, 
        t.EndTime, 
        t.TotalTime AS ElapsedTime
    FROM 
        Participants p
    JOIN 
        TimeResults t 
      ON p.IDParticipant = t.IDParticipant
    ORDER BY 
        t.TotalTime ASC
    """
    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results

@app.route('/')
def index():
    results = get_race_results()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
