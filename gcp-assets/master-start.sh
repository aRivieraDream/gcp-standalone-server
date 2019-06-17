#!/bin/bash
printf '\n\n-----Starting Tableau Server Scripted Install------\n'
gcloud deployment-manager deployments create tableau-standalone-server --config standalone-tableau-server.yaml
wait
printf '\n\n-----------\nThe VM has finished deploying but Tableau Server is still being installed ...\n'
IP=`gcloud compute instances describe tableau-server --zone=us-west1-a | grep natIP | awk '/natIP:/{print $NF}'`
SECRETS="https://console.cloud.google.com/storage/browser/tslinux-silent-install/static-assets"
printf "Tableau Server will take ~10 minutes to install.\n"
printf "Once the initial setup is complete and the files are downloaded onto the VM (~3 minutes) you can check the progress of the installation in your web browser. \n"
printf "\nTo check the progress, visit: \n https://$IP:8850 and login using your credentials. \n"
printf "\nLogin credentials can be found in the secrets file. If you are running this for the first time, download the screts file from... \n $SECRETS\n"
printf "\nNOTE: By default this IP address has no SSL certificate, so a modern browser may warn you of a security risk when logging into view the installation progress. \n\n"
printf "Once installation is finished, you can visit your server at: \n$IP\n"
