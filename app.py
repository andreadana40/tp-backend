from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL

# Jinja2 es un motor de plantillas que nos permite crear plantillas html dinamicas


app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] ='root'
app.config['MYSQL_DATABASE_PASSWORD'] ='tes3l6a9co'
app.config['MYSQL_DATABASE_DB'] = 'movies_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
    sql = "SELECT * FROM `movies_db`.`movies`" #Creo una consulta sql para obtener todas las movies
    conn = mysql.connect()#coneccion a base de datos
    cursor =conn.cursor()
    cursor.execute(sql)
    data_movies = cursor.fetchall()
    conn.commit()
    return render_template('movies/index.html', movies=data_movies)

@app.route('/create')
def create():
    return render_template('movies/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _name = request.form['name']
    _rating = request.form['rating']
    _awards = request.form['awards']
    _length = request.form['length']
    _genre_id =request.form['genre_id']


    sql = "INSERT INTO `movies_db`.`movies`(`created_at`,`updated_at`,`title`,`rating`,`awards`,`release_date`,`length`,`genre_id`) VALUES ( sysdate(), sysdate(),'" + _name +"', " + _rating + ", " + _awards + ", sysdate()," + _length +", " + _genre_id +");"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return 'Pelicula creada con exito'

@app.route('/delete/<id>')
def delete(id):
    sql = "DELETE FROM `movies_db`.`movies` WHERE `id` = " + id + ";"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return 'Pelicula eliminada con exito'

if __name__ == '__main__':
    app.run(debug=True)  