# web-meteostation

### Server instalatio
* `sudo apt-get install python-mysqldb`
* Create virtualenv (or not)
* `pip install -r requirements.pip`

### Daemon installation:
* Check if daemon scripts are executable. If not - `$ sudo chmod 755` for `.sh` and `.py` scripts.
* Copy the `temperature.py` script: `sudo cp -p temperature.py /opt/web-meteostation/`
* Copy the `temperature.sh` script: `sudo cp temperature.sh /etc/init.d/`
* Add the symb. links `sudo update-rc.d temperature.sh defaults`
* Start the daemon `sudo service temperature start`
