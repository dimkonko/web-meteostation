#!/bin/bash

# Because $0 is a file name of execution
function sql_run () {
    mysql -u $DB_USER -p < $1
}
