#!/bin/bash

source /vagrant/db/release/base_sql.sh

DB_USER="meteo"

sql_run "/vagrant/db/sql/data/insert_mock_data.sql"
