import redis
import string
import json
import sys

#Link up with redis 
r = redis.Redis(host='localhost', port=6379, db=0)


f = open('../Nutrition_Clean.json','r')
# Read one line from file

r.flushall()

list = []

for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
		line = json.loads(filter(lambda x: x in string.printable, line))
		
		for nut in line['nutrients']:
			r.zincrby('hashtag',nut['description'],1)
        	
length=r.zcard('hashtag')
val=r.zrange('hashtag',length-5,length)

for nut_tag in val:
	list.append(nut_tag)

print "### Top 5 most commonly occuring nutrients:"

i = 4
j = 1	
while i >= 0 :
	print j, '. ', list[i], ' occurs ', r.zscore('hashtag',list[i]), 'number of times'
	j += 1
	i -= 1