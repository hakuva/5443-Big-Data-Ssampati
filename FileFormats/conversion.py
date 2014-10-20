import yaml
import json

file = open('GpsFilePoints.yml')
data = yaml.load(file)
print json.dumps(data, sort_keys=True,indent=4, separators=(',', ': '))