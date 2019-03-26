
"""
Creates a virtual machine that runs ubuntu.
This template utilizes options selected in compute-engine-template.py
"""
# TODO:
# update image type to images/ubuntu-1604-xenial-v20181030
# figure out if 64 gigs of ram is really needed vs just the default 60
# double check scopes required


COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):
  """Creates a virtual machine suited for running Tableau server."""

  resources = [{
      'name': context.env['name'],
      'type': 'compute.v1.instance',
      'properties': {
          'zone': context.properties['zone'],
          'machineType': ''.join([COMPUTE_URL_BASE,
                                  'projects/', context.env['project'],
                                  '/zones/', context.properties['zone'],
                                  '/machineTypes/', context.properties['machineType']]),
          'minCpuPlatform': context.properties['minCpuPlatform'],
          'disks': [{
              'deviceName': 'boot', #why is this boot?
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/',
                                          'ubuntu-os-cloud/global/',
                                          'images/family/ubuntu-1604-lts']), #TODO: update to images/ubuntu-1604-xenial-v20181030
                  'diskType': ''.join(['projects/', context.env['project'],
                                       '/zones/', context.properties['zone'],
                                       '/diskTypes/', context.properties['diskType']]),
                  'diskSizeGb': context.properties['diskSizeGb']
              }
          }],
          'networkInterfaces': [{
              'network': ''.join([COMPUTE_URL_BASE,
                                  'projects/', context.env['project'],
                                  '/global/networks/', context.properties['network']]),
              'accessConfigs': [{
                  'name': 'External NAT',
                  'type': 'ONE_TO_ONE_NAT'
              }]
          }],
          'tags': {
            'items': [context.properties['tagName']]
          },
          'metadata': {
            'items': [
                {
                    'key': 'startup-script-url',
                    'value': 'gs://tslinux-silent-install/gcp-assets/startup-script.sh'
                }
            ]
          },
          'serviceAccounts': [
                {
                  'email': 'default',
                  'scopes': [
                    'https://www.googleapis.com/auth/devstorage.read_only',
                    'https://www.googleapis.com/auth/logging.write',
                    'https://www.googleapis.com/auth/monitoring.write',
                    'https://www.googleapis.com/auth/servicecontrol',
                    'https://www.googleapis.com/auth/service.management.readonly',
                    'https://www.googleapis.com/auth/trace.append'
                  ]
                }
            ]
        }
  }]
  return {'resources': resources}
