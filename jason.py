# import json
with open('user.json') as data_file:    
    data = json.load(data_file)

users = data['users']

for user in data:
  counter = 0
  print ("users full name is " + user['firstName'] + ' ' + user['lastName'])
  while counter < len(user['details']):
    print ("users mobile number is " + user['details'][counter]['mobileNo'])
    print ("users age  is " + user['details'][counter]['age'])
    print ("users city is " + user['details'][counter]['city'])
    counter=counter+1
