import redis
import sys
import json
import string

f= open('../Nutrition_Clean.json', 'r')

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.flushall()

for line in f:
	
	line = json.loads(filter(lambda x: x in string.printable, line))
	
	l = json.dumps(line)
	
	r.sadd('food_items',{line['description']})
	
	
print "### Unique food items in the given file:"
print "Unique Items:", r.scard('food_items')