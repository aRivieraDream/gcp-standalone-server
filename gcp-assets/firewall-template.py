def GenerateConfig(context):
  """
  Creates a firewall that is used to allow access on a bunch of ports in the
  default firewall for VM's with a particular tag.
  """

  resources = [{
      'name': context.env['name'],
      'type': 'compute.v1.firewall',
      'properties': {
          'description': 'Allows Tableau Server to be accessed by anyone. SSH required for admin, http for users, 8850 for setup',
          'network': ''.join([
                        '/projects/', context.env['project'],
                        '/global/networks/', context.properties['network']
          ]),
          'sourceRanges': ['0.0.0.0/0'],
          'allowed': [{
              'IPProtocol': 'TCP',
              'ports': [80,443,22,8850] #8850 for tsm, 22 for ssh
          }],
          'targetTags': [context.properties['tagName']]
      }
  }]
  return {'resources': resources}
