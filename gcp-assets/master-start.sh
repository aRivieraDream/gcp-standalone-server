#!/bin/bash

gcloud deployment-manager deployments create tableau-standalone-server --config standalone-tableau-server.yaml
wait
echo 'The VM has finished deploying but Tableau Server is still being installed ...'
IP=`gcloud compute instances describe tableau-server --zone=us-west1-a | grep natIP | awk '/natIP:/{print $NF}'`
echo "Tableau Server will take ~15 minutes to install. "
echo "Once the initial setup is complete (~5 minutes) you can check the progress of the installation in your web browser. "
echo "To check the progress, visit: /n $IP:8850 /n and login using your credentials."
echo "Once installation is finished, you can visit your server at $IP. Login credentials can be found in your secrets file."
