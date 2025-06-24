from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, static_folder='static')

<<<<<<< HEAD
def get_race_results(search_term=None):
=======
def get_race_results():
>>>>>>> d8cefe237ad5557a0cc56c897332c2da55a61540
    # Conéctate a la base de datos
    conn = mysql.connector.connect(
        host="sql10.freesqldatabase.com",
        user="sql10786405",
        password="ygewRIuATj",
        database="sql10786405",
        port=3306
    )
    cursor = conn.cursor(dictionary=True)

<<<<<<< HEAD
    # Base query
    base_query = """
=======
    # Consulta para obtener resultados
    query = """
>>>>>>> d8cefe237ad5557a0cc56c897332c2da55a61540
    SELECT 
        p.IDParticipant, 
        p.NameParticipant, 
        p.LastName_1, 
        p.LastName_2, 
        p.Category,
        t.StartTime, 
        t.EndTime, 
<<<<<<< HEAD
        t.TotalTime AS ElapsedTime,
        @rank := @rank + 1 AS Position
    FROM 
        Participants p
    JOIN 
        TimeResults t ON p.IDParticipant = t.IDParticipant,
        (SELECT @rank := 0) r
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
        query = base_query + search_condition + " ORDER BY t.TotalTime ASC"
        cursor.execute(query, (search_param, search_param, search_param, search_param))
    else:
        query = base_query + " ORDER BY t.TotalTime ASC"
        cursor.execute(query)
    
    results = cursor.fetchall()
=======
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

>>>>>>> d8cefe237ad5557a0cc56c897332c2da55a61540
    cursor.close()
    conn.close()

    return results

@app.route('/')
def index():
    search_term = request.args.get('search', None)
    results = get_race_results(search_term)
    return render_template('index.html', results=results, search_term=search_term)

if __name__ == '__main__':
    app.run(debug=True)
