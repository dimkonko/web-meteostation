#!/bin/bash

PROJECT_NAME="meteo.com"

export PROJECT_NAME=$PROJECT_NAME

echo "# Updating the cache..."
apt-get update

echo "# Installing apache2..."
apt-get -y install apache2

echo "# Installing php5"
apt-get -y install php5 libapache2-mod-php5

debconf-set-selections <<< 'mysql-server mysql-server/root_password password 123456'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password 123456'
echo "Installing mysql"
apt-get -y install mysql-server-5.5 libapache2-mod-auth-mysql php5-mysql

# echo "# Setup project"
# mkdir -p /var/www/$PROJECT_NAME/public_html
# cp -f /vagrant/etc/VirtualHost.conf /etc/apache2/sites-available/$PROJECT_NAME.conf

# echo "# Enabling $PROJECT_NAME"
# sudo a2ensite $PROJECT_NAME.conf

echo "# Restarting apache"
service apache2 restart
