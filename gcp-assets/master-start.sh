#!/bin/bash

gcloud deployment-manager deployments create tableau-standalone-server --config standalone-tableau-server.yaml
wait
printf '\n\n-----------\nThe VM has finished deploying but Tableau Server is still being installed ...\n'
IP=`gcloud compute instances describe tableau-server --zone=us-west1-a | grep natIP | awk '/natIP:/{print $NF}'`
printf "Tableau Server will take ~10 minutes to install.\n "
printf "Once the initial setup is complete (~3 minutes) you can check the progress of the installation in your web browser. \n"
printf "To check the progress, visit: \n https://$IP:8850 \n and login using your credentials. Note that this IP address has no SSL certificate, so a modern browser may warn you of a security risk. \n\n"
printf "Once installation is finished, you can visit your server at: \n$IP \nLogin credentials can be found in your secrets file."
