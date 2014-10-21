import redis
import string
import json
import sys

#Link up with redis 
r = redis.Redis(host='localhost', port=6379, db=0)


f = open('../Nutrition_Clean.json','r')
# Read one line from file

r.flushall()

def memory():
	mem_info=str(r.info())
	mem_info=mem_info.replace('\'','"')
	mem_val=json.loads(filter(lambda x: x in string.printable, mem_info))
	print "Total Memory used to perform the opeations is: ", mem_val['used_memory']


for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
		line = json.loads(filter(lambda x: x in string.printable, line))
		
		for nut in line['nutrients']:
			r.sadd("nutri",nut['_id'])
			r.hset("nutri_hash",nut['_id'],nut)
			r.sadd("nutri_tag",nut['tagname'])
			r.hset("nutri_tag_hash",nut['tagname'],nut)
		
print "### Size of the database depending on how data is stored."
memory()