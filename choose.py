import sys
import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
  username="a1582e86-98b0-4041-8fac-9c01aa85f964",
  password="kiDEgM7oCRW7",
  version="2017-08-01"
)

qopts = {'query': 'IBM', 'filter': 'score', ...}
my_query = discovery.query('bf72d33c-369d-41a0-80b3-90e11c26ab52', '2fcd4c3b-d355-4451-b0c8-7640527ba546', qopts)
print(json.dumps(my_query, indent=2))