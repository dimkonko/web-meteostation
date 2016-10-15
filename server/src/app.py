import pytz

import config_provider
import queries

from datetime import datetime

from flask import (
    Flask,
    render_template,
    request,
    abort
)

from db_api import MySQLApi

app = Flask(__name__)
config_provider.init_config(app)

mysqlapi = MySQLApi(config=app.config['DB'])

last_insert = None


def set_last_insert(t, h, create_date):
    print "update"
    global last_insert
    last_insert = {
        'temperature': int(t),
        'humidity': int(h),
        # Fri 14, October 2016 at 08:22 AM
        'create_date': datetime.strptime(create_date, "%Y-%m-%d %H:%M:%S").strftime("%a %d, %B %Y at %I:%M %p")
    }


def is_data_changed(t, h):
    data_changed = False
    if not last_insert or (t != last_insert['temperature'] or h != last_insert['humidity']):
        data_changed = True
    return data_changed


def is_data_valid(t, h):
    valid = False
    if t != 0 and h != 0:
        valid = True
    return valid


def initialize():
    # Get [0], because there should be only 1 record
    last_record = mysqlapi.get(queries.GET_LAST_RECORD)
    if last_record:
        print "insert"
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
    t = int(request.form.get('t', 0))
    h = int(request.form.get('h', 0))
    create_date = request.form.get('create_date', datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S"))

    if not is_data_valid(t, h):
        return abort(400)

    # Insert data only if it's different from previous
    if is_data_changed(t, h):
        mysqlapi.set(queries.INSERT_RECORD, t, h, create_date)
        initialize()

    return 'ok'
