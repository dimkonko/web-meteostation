#!/bin/bash

source /vagrant/db/release/base_sql.sh

DB_USER="root"

sql_run "/vagrant/db/sql/create_db.sql"
sql_run "/vagrant/db/sql/create_tables.sql"
sql_run "/vagrant/db/sql/create_users.sql"
