#import 
import json
FILE = open('eq_data.json', 'r')
eq = json.load(FILE)

#1) print out the number of earthquakes
print("The number of earthquakes is:", eq["metadata"]["count"])

#2) iterate through the dictionary and extract the location, magnitude, 
   #longitude and latitude of the location and put it in a new
   #dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
   #magnitude > 6. Print out the new dictionary.

list_eq = eq['features']
eq_dict = {'location': [], 'magnitude': [], 'longitude': [], 'latitude': []}
eq_dict1 = {}

for eq in list_eq:
   location = eq['properties']['place']
   if eq['properties']['mag'] >6:
      eq_dict1[location] = {'mag': eq['properties']['mag'], 'lat': eq['geometry']['coordinates'][1], 'lon': eq['geometry']['coordinates'][0]}

i = 0

for k,j in eq_dict1.items():
   if i < 3:
      print('Location', k)
      print('Magnitude', j['mag'])
      print('Latitude', j['lat'])
      print('Longitude', j['lon'])
      print()
      i += 1

'''
for earthquakes in earth_list:
   if earthquakes['properties']['mag'] > 6:
      eq_dict['location'].append(earthquakes['properties']['place'])
      eq_dict['magnitude'].append(earthquakes['properties']['mag'])
      eq_dict['longitude'].append(earthquakes['geometry']['coordinates'][0])
      eq_dict['latitude'].append(earthquakes['geometry']['coordinates'][1])
print(eq_dict)
print()

#3) using the eq_dict dictionary, print out the information as shown below:
i = 0
while i <= 3:
   for k,j in eq_dict.items():
      print(k, ':', j[i]) 
   i += 1
   print()

'''




