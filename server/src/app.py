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

last_insert = None


@app.route('/')
def index():
    data = mysqlapi.get_meteo_data()
    return render_template('index.html', data=data)


@app.route('/add_data', methods=["POST"])
def add_data():
    t = request.form['t']
    h = request.form['h']
    create_date = request.form['create_date']

    # Insert data only if it's different from previous
    global last_insert
    if not last_insert or is_data_changed(t, h, create_date):
        print "insert"
        mysqlapi.insert_meteo_data(t, h, create_date)

    last_insert = {
        't': t,
        'h': h,
        'create_date': create_date
    }
    print last_insert
    return 'ok'


def is_data_changed(t, h, create_date):
    data_changed = True
    if t == last_insert['t'] and h == last_insert['h']:
        data_changed = False
    return data_changed
