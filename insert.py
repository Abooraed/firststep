from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
import mysql.connector

# Function to connect to the MySQL database
def connect_to_mysql():
    host = "localhost"
    user = "root"
    password = ""
    database = "erstc"

    # Create the connection
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    return conn

# Function to execute a SELECT query in MySQL
def select_data(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM formulairee"
    cursor.execute(query)
    results = cursor.fetchall()
    return results

# Function to display the details page
def show_details_page():
    conn = connect_to_mysql()
    results = select_data(conn)

    put_html('<center><h3>Details</h3></center>').style('background-color:#25316D;color:gold; padding:25px;')

    # Create a table to display the data
    table_data = [('ID', 'Équipe', 'Lieu', 'Date', 'Nature')]
    table_data.extend(results)  # Add the retrieved data to the table

    put_table(table_data)  # Display the table

# Function to insert data into MySQL
def insert_data(conn, id, equipe, lieu, date, nature, file_data):
    cursor = conn.cursor()
    query = "INSERT INTO formulairee (id, equipe, lieu, date, nature, file_data) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (id, equipe, lieu, date, nature, file_data)
    cursor.execute(query, values)
    conn.commit()

def insert():
    put_html('<center><h3>Formulaire à Remplir</h3></center>').style('background-color:#40513B;color:#EDF1D6; padding:25px;')
    put_html('<p>ETABLISSEMENT REGIONAL SUPPORT TECHNIQUE AU COMMERCIAL</p>').style('text-align:center;font-weight:bold;')
    put_image('https://recruteur.lefigaro.fr/wp-content/uploads/2020/09/Sans-titre-25.png', width='1000px').style('border-radius:15px;')

    data = input_group(
        'Remplir le Formulaire', 
        [   
            input('ID', name='id'),
            input('ÉQUIPE', name='equipe'),
            input('LIEU', name='lieu'),
            input('DATE', name='date', type=DATE),
            input('NATURE', name='nature'),
            input('Fichier', name='file_data')
        ]
    )

    put_buttons(['Afficher les détails'], onclick=[show_details_page])

    conn = connect_to_mysql()
    insert_data(conn, data['id'], data['equipe'], data['lieu'], data['date'], data['nature'], data['file_data'])
    put_text("Données insérées avec succès dans la base de données.")

start_server(insert, port=3335, debug=True)