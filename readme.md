## About Standalone Server Install
This project provides the resources required to programmatically stand up a single instance of Tableau Server 2019.1 on GCP. **The default setting of this project automatically accepts Tableau's [End User Licence Agreement](https://mkt.tableau.com/files/tableau_eula.pdf) (EULA).** It's important that you read this agreement and understand what you are accepting if you haven't done so before.

The project is separated into two sections, `gcp-assets` and `static-assets`. `static-assets` contains all of the assets that are used by Tableau during the installation process. Some of these assets include files which you may want to modify in order to configure the installation to your particular needs. `gcp-assets` contains configuration files used to define the VM and firewall settings required to run Tableau server, and it also contains a couple of master scripts to quickly create and destroy your project in GCP.

This project was originally created to run on a machine that runs linux commands. Currently, even though everything should work the same on machines running Windows, we cannot guarantee Windows support with this product.

## Costs
By running this software, you will create GCP resources that you will be billed for. That said, included is a way to quickly remove any newly created assets. By executing this project and then subsequently destroying the newly created assets by running the `./master-destroy.sh` script, the total cost should only be a few dollars (depending on your billing agreement with Google). If left running, the VM that runs Tableau server could cost you a few hundred dollars per month.

## Prerequisits
In order to run this project you must have the following:
1. Read and understand the Tableau [EULA](https://mkt.tableau.com/files/tableau_eula.pdf)
*  [gcloud command-line tool](https://cloud.google.com/sdk/gcloud/) installed on your computer
*  Have a [default project](https://cloud.google.com/sdk/docs/configurations#setting_configuration_properties) set to your gcloud command
*  Have [IAM permission](https://cloud.google.com/compute/docs/access/iam) to create both compute resources and firewall rules
*  Have a 'default' GCP VPC Network (GCP gives every project this by default)

## How to Use This
1. Download the `gcp-assets file`
* make sure that `master-start.sh` is set as an executable and run `./master-start.sh`
* After you run the script, it will take 15-20 minutes to install tableau server. If you'd like to check the process, follow the instructions in your console output.

## Configurations
The current settings for this project are configured to be as permissible as possible to facilitate the easy installation and trial of Tableau Server on GCP. Because of this, it's important to reconfigure these settings once you are ready to deploy in a production environment.

Here are some of the configurations you might want to consider during a production deployment:
1. Add your licence key and registration information in `reg_templ.json`
* Create your own GCP bucket where you store a modified version of these resources.
  -  Edit line 59 of `vm-template.py` to point to the correct location of your startup script.
* Modify the Tableau admin username and password in `secrets`
* Update your desired zone in `compute-engine-template.py` and in `master-start.sh`
 - Note that most of the variables in `compute-engine-template.py` are set to recommended Tableau Server configuration and won't need modification
* Change your [identity store](https://onlinehelp.tableau.com/current/server-linux/en-us/config_general.htm) from local to Active Directory by modifying the `config.json`
* Modify firewall rules in `firewall-template.py` to restrict traffic only to certain IP addresses
