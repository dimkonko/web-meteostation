# web-meteostation

### Daemon installation:
* Check if daemon scripts are executable. If not - `$ sudo chmod 755` for `.sh` and `.py` scripts.
* Copy the `temperature.sh` script to ``/etc/init.d/` folder with `$ sudo cp temperature.sh /etc/init.d/`
* Add the symb. links `sudo update-rc.d temperature.sh defaults`
* Start the daemon `sudo service temperature start`
