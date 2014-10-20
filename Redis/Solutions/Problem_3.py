import redis
import string
import json
import sys

#Link up with redis 
r = redis.Redis(host='localhost', port=6379, db=0)


f = open('../Nutrition_Clean.json','r')
# Read one line from file

r.flushall()

for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
		line = json.loads(filter(lambda x: x in string.printable, line))
		
		for nut in line['nutrients']:
			r.zincrby('taghash',nut['description'],1)
        	
LenZList=r.zcard('taghash')
listVals=r.zrange('taghash',LenZList-5,LenZList)

for test in listVals:
	print test
	print r.zscore('taghash',test)