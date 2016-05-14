#!/bin/bash

source /vagrant/db/release/base_sql.sh

DB_USER="newuser"

sql_run "/vagrant/db/sql/create_db.sql"
sql_run "/vagrant/db/sql/create_tables.sql"
