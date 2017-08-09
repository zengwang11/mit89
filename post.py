import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
  username="a1582e86-98b0-4041-8fac-9c01aa85f964",
  password="kiDEgM7oCRW7",
  version="2017-08-01"
)

response = discovery.create_environment(
  name="my_environment",
  description="My environment",
  size=1
)

print(json.dumps(response, indent=2))