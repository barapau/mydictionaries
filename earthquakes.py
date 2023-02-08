#import 
import json
FILE = open ('eq_data.json')
earth_dic = json.load(FILE)

#1) print out the number of earthquakes
print("The number of earthquakes is:", earth_dic["metadata"]["count"])

#2) iterate through the dictionary and extract the location, magnitude, 
   #longitude and latitude of the location and put it in a new
   #dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
   #magnitude > 6. Print out the new dictionary.

earth_list = earth_dic['features']
eq_dict = {'location':[], 'magnitude':[], 'longitude':[], 'latitude':[]}

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
while i <= 2:
   for k,j in eq_dict.items():
      print(k, ':', j[i]) 
   i += 1
   print()


