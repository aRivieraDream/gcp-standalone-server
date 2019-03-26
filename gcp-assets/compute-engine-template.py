
"""Creates the Compute Engine Resources"""

NETWORK_NAME = 'default' # if this changes you need to replace with selflinks in both vm and firewall
TAG_NAME = 'tableau-server'

def GenerateConfig(unused_context):
    """These resources are used to define parameters needed for vm-template.py """

    resources = [{
        'name': 'tableau-server',
        'type': 'vm-template.py',
        'properties': {
            'machineType': 'n1-standard-16', #used in machineType
            'diskType': 'pd-ssd', #used in machineType
            'diskSizeGb': '128',
            'minCpuPlatform': 'Intel Skylake', #used in machineType
            'zone': 'us-west1-a', #used in machineType
            'network': NETWORK_NAME, #used in machineType
            'tagName': TAG_NAME #used to ensure firewall is open
        }
    } , {
        'name': NETWORK_NAME + '-tableau-server',
        'type': 'firewall-template.py',
        'properties': {
            'network': NETWORK_NAME,
            'tagName': TAG_NAME
        }
    }]
    return {'resources': resources}
