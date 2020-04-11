#!/usr/bin/env bash
# that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "
<html>
    <head></head>
    <body>
        Holberton School
    </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "/# Only/ i location /hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-enabled/default
sudo service nginx restart

