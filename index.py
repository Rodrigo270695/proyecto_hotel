from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3307
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'hotel'
mysql.init_app(app)


""" principal """


@app.route('/')
def principal():

    return render_template('index.html')

""" home """

@app.route('/home')
def home():

    return render_template('home.html')


""" nueva habitacion """


@app.route('/nueva_habitacion')
def nuevahabitacion():

    return render_template('item-new.html')


""" almacenar datos de habitacion """


@app.route('/store', methods=['POST'])
def storage():

    _numero = request.form['item_numero']
    _tipo = request.form.get('item_tipo')
    _estado = request.form.get('item_estado')

    datos = (_numero, _tipo, _estado)

    sql = "INSERT INTO `habitaciones` (`id`, `numero`, `tipo`, `estado`) VALUES (NULL,%s,  %s, %s);"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    return render_template('item-new.html')


""" lista  habitacion """


@app.route('/lista_habitacion')
def listahabitacion():

    sql = "SELECT * FROM `habitaciones`;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    habitacion = cursor.fetchall()
    print(habitacion)
    conn.commit()

    return render_template('item-list.html', habitacion=habitacion)


""" editar habitacion """


@app.route('/edit/<int:id>')
def edithabitacion(id):

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id,numero, tipo, estado FROM habitaciones WHERE id=%s", (id))
    habitacion = cursor.fetchone()
    print(habitacion)
    conn.commit()

    return render_template('item-update.html', habitacion=habitacion)


""" actualizar habitacion """


@app.route('/update', methods=['POST'])
def actualizarhabitacion():

    _numero = request.form['item_numero']
    _tipo = request.form.get('item_tipo')
    _estado = request.form.get('item_estado')
    id = request.form['item_codigo']

   
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE habitaciones SET numero = %s, tipo=%s, estado =%s   WHERE id=%s",
                   (_numero, _tipo, _estado, id))
    conn.commit()

    return redirect('/lista_habitacion')


""" eliminar habitacion """


@app.route('/destroy/<int:id>')
def destroy(id):

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM habitaciones WHERE id=%s", (id))
    conn.commit()
    return redirect('/lista_habitacion')


""" nuevo cliente  """


@app.route('/nuevo_cliente')
def nuevo_cliente():

    return render_template('client-new.html')


""" almacenar datos de cliente"""


@app.route('/store_cliente', methods=['POST'])
def store_cliente():

    _dni = request.form['cliente_dni']
    _nombre = request.form['cliente_nombre']
    _apellido = request.form['cliente_apellido']
    _telefono = request.form['cliente_telefono']
    _direccion = request.form['cliente_direccion']

    datos = (_dni, _nombre, _apellido, _telefono, _direccion)

    sql = "INSERT INTO `cliente` (`id`, `dni`,`nombre`, `apellido`, `telefono`, `direccion`) VALUES (NULL,%s,  %s, %s, %s, %s);"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    return render_template('client-new.html')


""" lista cliente"""


@app.route('/lista_cliente')
def lista_cliente():

    sql = "SELECT * FROM `cliente`;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    cliente = cursor.fetchall()
    print(cliente)
    conn.commit()

    return render_template('client-list.html', cliente=cliente)


""" editar cliente """


@app.route('/edit_cliente/<int:id>')
def edit_cliente(id):

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, dni, nombre, apellido, telefono, direccion  FROM cliente WHERE id=%s", (id))
    cliente = cursor.fetchone()
    print(cliente)
    conn.commit()

    return render_template('client-update.html', cliente=cliente)


""" actualizar cliente """


@app.route('/update_cliente', methods=['POST'])
def actualizar_cliente():

    _dni = request.form['cliente_dni']
    _nombre = request.form['cliente_nombre']
    _apellido = request.form['cliente_apellido']
    _telefono = request.form['cliente_telefono']
    _direccion = request.form['cliente_direccion']
    id = request.form['cliente_codigo']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE cliente SET dni = %s, nombre=%s, apellido =%s, telefono =%s , direccion =%s  WHERE id=%s",
                   (_dni, _nombre, _apellido,  _telefono, _direccion,  id))

    conn.commit()

    return redirect('/lista_cliente')



""" eliminar cliente """


@app.route('/eliminar_cliente/<int:id>')
def eliminar_cliente(id):

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cliente WHERE id=%s", (id))
    conn.commit()
    return redirect('/lista_cliente')




""" nueva reserva """


@app.route('/nueva_reservacion')
def nueva_reserva():

    return render_template('reservation-new.html')

@app.route('/lista_reserva')
def lista_reserva():

    return render_template('reservation-list.html')
    


if __name__ == '__main__':
    app.run(debug=True, port=5017)



    #integrantes
    #Gonzales Manay Cristian
    #Chozo Riojas Ricardo
    #Bravo Cabrejos Edwin
    #Dvila Nieto Justo

