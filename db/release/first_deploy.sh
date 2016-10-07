#!/bin/bash

source base_sql.sh

DB_USER="root"

sql_run "../sql/create_db.sql"
sql_run "../sql/create_tables.sql"
sql_run "../sql/create_users.sql"
