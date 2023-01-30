person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #value is a list
person["pets"] = {"dog": "Fido", "cat": "Sox"} #value is another dictionary

print(person)

#name of  the second child
print(person.get("children")[1]) #doesnt give error if it doesnt  exist 
print(person["children"][1]) #best solution

print(type(person["children"])) #which kind of element im dealing with 


#the name of the cat
print(type(person["pets"]))
print(person["pets"]["cat"])

#use a  for loop to list each child
for i in person["children"]:
    print(i)

#print out  the pets in this format
#'Type of pet: dog name of pet: Fio 
for i,j in  person['pets'].items():
    print(f"Type of pet:{i} name of pet: {j}")
#the key being i and the  j being value  