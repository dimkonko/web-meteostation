<?php
class MeteoDB {
    private $_connection;

    /**
     * Connect to the db
     *
     * @return {boolean} - false on error; true on success
     */
    private function _connect() {
        $config = parse_ini_file('./conf.ini');

        $this->$connection = new mysqli($config['servername'], $config['username'],
            $config['password'], $config['dbname']);

        // Check connection
        if($this->$connection === false) {
            // Handle error - notify administrator, log to a file, show an error screen, etc.
            return false;
        }
    }

    private function _disconnect() {
        $this->$connection->close();
    }

    private function _execute($sql) {
        $this->_connect();
        $result = $this->$connection->query($sql);
        $this->_disconnect();
        return $result;
    }

    public function getMeteoData() {
        $data;
        $sql = "SELECT * FROM METEO_DATA_SMART_HOUSE WHERE create_date = (select MAX(create_date) from METEO_DATA_SMART_HOUSE);";
        $result = $this->_execute();
        return $rows;
    }
}
?>