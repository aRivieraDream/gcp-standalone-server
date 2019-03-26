#!/bin/bash
#
# Runs all commands necessary to install Tableau Server on GCP assuming static assets are downloaded in current folder.
set -euxo pipefail
sudo apt-get update

# tslinux-silent-install/static-assets files are all stored with default information for trial
# If you're using this template to configure your own deployment replace this location with wherever
# you are storing your registration, config, secrets, and server.deb files.
sudo gsutil -m cp -r gs://tslinux-silent-install/static-assets/ ~/
cd ~/static-assets/

# Create dummy user from secrets file for installing tsm
. secrets
sudo printf "$tsm_admin_pass\n$tsm_admin_pass\n\n\n\n\nY\n" | sudo adduser $tsm_admin_user
sudo usermod -aG sudo $tsm_admin_user

# modify installer script to be an executable
sudo chmod +x automated-installer

# Run the installer as dummy user (-a flag)
sudo ./automated-installer -s secrets -f config.json -r reg_templ.json --accepteula -a $tsm_admin_user tableau-server-2019-1-1_amd64.deb

# cleanup files used for install
cd ..
sudo rm -r static-assets/
