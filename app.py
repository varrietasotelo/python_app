from flask import Flask, render_template
import database as dbase
from casos import casos 

db = dbase.dbConnection()

app = Flask(__name__)

#rutas
@app.route('/')
def home():
    casos = db['casos']
    Recived = casos.find()
    return render_template('index.html', casos = Recived)


if __name__ == '__main__':
    app.run(debug=True, port=4000)