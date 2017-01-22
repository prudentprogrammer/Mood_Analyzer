import json 
import pprint
import datetime
import random
json_string = open('totalSentiment.json').read()
parsed_json = json.loads(json_string)


#map_months = {
#    1: 'Jan',
#    2: 'Feb',
#    3: 'Mar',
#    4: 'Apr',
#    5: 'May',
#    6: 'Jun',
#    7: 'Jul',
#    8: 'Aug',
#    9: 'Sep',
#    10: 'Oct',
#    11: 'Nov',
#    12: 'Dec'
#}
#
#days = [x for x in range(1, 31)]
#months = [map_months[x] for x in range(1, 13) ]
#year = 2016

date = datetime.datetime(2016,1,1)
print len(parsed_json)

for i in range(len(parsed_json)):
    
    corrected_format = '{:%d-%b-%Y}'.format(date)
    parsed_json[i]["date"] = corrected_format
    date += datetime.timedelta(days=1)

    

for sentiment in parsed_json:
    x = random.random()
    x = round(x, 6)
    sentiment["docSentiment"]["score"] = x
"""
for sentiment in parsed_json:
    #for attribute, value in song.iteritems():
    #    print attribute, value # example usage
    temp = ["date"]
    temp_tuple = tuple(temp)
    parsed_json["date"] = date
    date += datetime.timedelta(days=1)
    print parsed_json["date"]

"""
pprint.pprint(parsed_json)