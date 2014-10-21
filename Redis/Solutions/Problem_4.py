import redis
import sys
import json
import string

f= open('../Nutrition_Clean.json', 'r')

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.flushall()

for line in f:

    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
		line = json.loads(filter(lambda x: x in string.printable, line))
		
	
		r.sadd('food_items',{line['description']})
	
		for nut in line['nutrients']:
				r.zincrby('hashtag',nut['description'],1)


item = 'Protein'	
num_items = r.scard('food_items')
item_rep = r.zscore('hashtag',item)
print "### Percentage of food items contain ",item," nutrient:"
print "> Unique Items:", num_items
print "> ",item, ' occurs ',item_rep,' times'

per = (float(item_rep)/float(item_rep))*100
print "> ",item, " occurs in " , per , "% number of food items."