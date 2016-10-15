import config_provider
import app_service
import date_service
import template_records_factory
import queries

from flask import (
    Flask,
    render_template,
    request,
    abort
)

from db_api import MySQLApi
from last_record_storage import LastRecordStorage

app = Flask(__name__)
config_provider.init_config(app)

mysqlapi = MySQLApi(config=app.config['DB'])
last_record_storage = LastRecordStorage()


def init_last_update_record():
    # Get [0], because there should be only 1 record
    last_record = mysqlapi.get(queries.GET_LAST_RECORD)
    if last_record:
        last_record = last_record[0]
        last_record_storage.init_record(last_record['temperature'], last_record['humidity'],
                                        last_record['create_date'])


init_last_update_record()


@app.route('/')
def index():
    data = mysqlapi.get(queries.GET_ALL_RECORDS)
    last_record = last_record_storage.get_record()
    return render_template('index.html', data=template_records_factory.get_records(data),
                           has_last_update=last_record_storage.has_record(),
                           last_update=template_records_factory.create_from_last_update(last_record))


@app.route('/add_data', methods=["POST"])
def add_data():
    t = int(request.form.get('t', 0))
    h = int(request.form.get('h', 0))
    create_date = request.form.get('create_date', date_service.get_now())

    if not app_service.is_data_valid(t, h):
        return abort(400)

    # Insert data only if it's different from previous
    if last_record_storage.has_data_changed(t, h):
        print "i"
        record = last_record_storage.init_record(t, h, create_date)
        mysqlapi.set(queries.INSERT_RECORD, record.t, record.h,
                     date_service.get_formated_date(record.create_date))
    else:
        print 'u'
        last_record_storage.set_last_update_date(create_date)

    return 'ok'
