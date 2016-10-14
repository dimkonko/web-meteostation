import config_provider
import queries

from datetime import datetime

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


def set_last_insert(t, h, create_date):
    global last_insert
    last_insert = {
        'temperature': t,
        'humidity': h,
        # Fri 14, October 2016 at 08:22 AM
        'create_date': datetime.strptime(create_date, "%Y-%m-%d %H:%M:%S").strftime("%a %d, %B %Y at %I:%M %p")
    }
    print last_insert


def is_data_changed(t, h):
    data_changed = True
    if last_insert and t == last_insert['temperature'] and h == last_insert['humidity']:
        data_changed = False
    return data_changed


def initialize():
    # Get [0], because there should be only 1 record
    last_record = mysqlapi.get(queries.GET_LAST_RECORD)
    if last_record:
        last_record = last_record[0]
        set_last_insert(str(last_record['temperature']), str(last_record['humidity']), str(last_record['create_date']))


initialize()


@app.route('/')
def index():
    global last_insert
    data = mysqlapi.get(queries.GET_ALL_RECORDS)
    has_last_update = last_insert is not None
    return render_template('index.html',
                           data=data, has_last_update=has_last_update, last_update=last_insert)


@app.route('/add_data', methods=["POST"])
def add_data():
    t = request.form['t']
    h = request.form['h']
    create_date = request.form['create_date']

    # Insert data only if it's different from previous
    if is_data_changed(t, h):
        print 'insert'
        mysqlapi.set(queries.INSERT_RECORD, t, h, create_date)

    set_last_insert(t, h, create_date)
    return 'ok'
