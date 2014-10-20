import redis
import sys
import json
import string

f= open('nutrition.json', 'r')

count = 0

Checking = []
Check = []
Counter = []

for line in f:
	line = json.loads(filter(lambda x: x in string.printable, line))
	
	l = json.dumps(line)
	
	if (len(Check) == 0):
		Check.append(line['description'])
		
	else:
		j = 0
		for j in range((len(Check))-1):
			if (Check[j] == line['description']):
				k = 1
		if k == 0:
			Check.append(line['description'])
	
	for nut in line['nutrients']:
		k=0
		if (len(Checking) == 0):
			Checking.append(nut['description'])
			Counter.append(1)
		
		else:
			j = 0
			for j in range((len(Checking))-1):
				if (Checking[j] == nut['description']):
					Counter[j] = Counter[j] + 1
					k = 1
					
			if k == 0:
				Checking.append(nut['description'])
				Counter.append(1)

ind = Counter.index(max(Counter))
per = ((len(Check))/(max(Counter))) * 100
print Checking[ind], " occurs in ", per, "% number of food items."