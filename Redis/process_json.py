import string
import json

def is_json(myjson):
   try:
      json_object = json.loads(myjson)
   except ValueError, e:
      return False
   return True

file1 = open('nutrition.json','r')
file2 = open('Nutrition_Clean.json','w')
writeup = open('writeup.md','w')

count1 = 0
count2 = 0
count3 = 0.0

# Read one line from file
for line in file1:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
        if is_json(line):
            count1=count1+1
            line = json.loads(filter(lambda x: x in string.printable, line))
            out = json.dumps(line)
            file2.write(out)
        else:
            count2=count2+1
count3 = float((count2/count1)*100)
writeup.write('### Json File Processing')
writeup.write('\n### Written by Sai Sharan Sampati')
writeup.write('\n- Total Lines Processed: ' +str(count1))
writeup.write('\n- Total Lines Remove: : ' +str(count2))
writeup.write('\n- Ratio of Good Vs Bad: %0.5f' % count3)