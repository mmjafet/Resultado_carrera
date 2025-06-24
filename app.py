from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, static_folder='static')

def get_race_results(search_term=None):
    # Conéctate a la base de datos
    conn = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10786405",
        password="ygewRIuATj",
        database="sql10786405",
        port=3306
    )
    cursor = conn.cursor(dictionary=True)

    # Base query - corregida para usar ElapsedTime en lugar de TotalTime
    base_query = """
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
    """
    
    # Add search condition if search term is provided
    if search_term:
        search_condition = """
        WHERE 
            p.NameParticipant LIKE %s OR 
            p.LastName_1 LIKE %s OR 
            p.LastName_2 LIKE %s OR 
            p.IDParticipant LIKE %s
        """
        search_param = f"%{search_term}%"
        query = base_query + search_condition + " ORDER BY t.ElapsedTime ASC"
        cursor.execute(query, (search_param, search_param, search_param, search_param))
    else:
        query = base_query + " ORDER BY t.ElapsedTime ASC"
        cursor.execute(query)
    
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return results

@app.route('/')
def index():
    search_term = request.args.get('search', None)
    results = get_race_results(search_term)
    # Pasar request a la plantilla para acceder a request.args
    return render_template('index.html', results=results, request=request)

if __name__ == '__main__':
    app.run(debug=True)
