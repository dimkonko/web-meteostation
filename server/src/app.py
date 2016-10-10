import config_provider

from flask import (
    Flask,
    session,
    render_template,
    request,
    redirect,
    abort
)

from db_api import MySQLApi


app = Flask(__name__)
config_provider.init_config(app)


mysqlapi = MySQLApi(config=app.config['DB'])


@app.route('/')
def index():
    data = mysqlapi.get_meteo_data()
    return render_template('index.html', data=data)


@app.route('/add_data', methods=["POST"])
def add_data():
    t = request.form['t']
    h = request.form['h']
    create_date = request.form['create_date']
    mysqlapi.insert_meteo_data(t, h, create_date)
    return 'ok'
