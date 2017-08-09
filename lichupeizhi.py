import sys
import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
  username="3a7bed13-74f2-4f8f-b637-7fdf416e659f",
  password="AdDuFYC38Tlj",
  version="2017-08-01"
)

configs = discovery.list_configurations({'environment_id'})
print(json.dumps(configs, indent=2))
