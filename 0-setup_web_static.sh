#!/usr/bin/env bash
#setup server conf for the deployment of web_static files

#1. install nginx
sudo apt-get update -y
sudo apt-get install nginx -y

#2. Create directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/releases/test/

#3. Create HTML file (test file)
sudo touch /data/web_static/releases/test/index.html
echo "RC test page" | sudo tee /data/web_static/releases/test/index.html

#4. Create a symbolic link /data/web_static/current linked to 
# the /data/web_static/releases/test/ folder. If the symbolic link already
# exists, it should be deleted and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#5. Give ownership of the /data/ folder to the ubuntu user AND group (you
# can assume this user and group exist). This should be recursive; everything
# inside should be created/owned by this user/group.
sudo chown -hR ubuntu:ubuntu /data/

#6. Update the Nginx config to serve the content of /data/web_static/current/
# to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Dont forget to
# restart Nginx after updating the config: Use alias inside your Nginx config

sudo sed -i '53i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
sudo service nginx restart
