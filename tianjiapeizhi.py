import sys
import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
  username="3a7bed13-74f2-4f8f-b637-7fdf416e659f",
  password="AdDuFYC38Tlj",
  version="2017-08-01"
)

with open(os.path.join(os.getcwd(), 'config.json')) as config_data:
  data = json.load(config_data)
  new_config = discovery.create_configuration('40f75e61-6987-431c-b14d-c746b9918a3e,' data)
print(json.dumps(new_config, indent=2))
