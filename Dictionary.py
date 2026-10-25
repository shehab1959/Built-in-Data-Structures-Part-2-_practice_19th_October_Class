#Dictionary {"key":"value"}

d = {"name":"Shehab", "age":20, "work":"None"}
print(d) #{'name': 'Shehab', 'age': 20, 'work': 'None'}
print(type(d)) #dict
print(len(d)) #3


#create dict using function
dd = dict(name = "Shb", age = 22, work = "Unemplyed")
print(dd) #{'name': 'Shb', 'age': 22, 'work': 'Unemplyed'}
print(type(dd)) #dict


#No indexing
ddd = {"name":"Shehab", "age":20, "work":"None", 1:"Moja"}
print(ddd[1]) #Moja
#print(ddd[0]) #error


#alternative way to write dict
d = {
    "name":"Shehab",
    "age":20,
    "work":"None",
    1:"Moja"
}
#use get() methods
print(d["name"]) #Shehab
print(d.get("name")) #Shehab

#print(d["city"]) #error, as no "city" key
print(d.get("city")) #None, no error because of use get(), if not available then just show "none"
print(d.get("city", "not found")) #not found, default show "not found" as "city" key not available
print(d.get("name", "not found")) #Shehab, as "name" value available
print(d.get(1, "not found")) #Moja, as 1 value available



##Some Dictionary Methods
d = {
    "name":"Hejbulla",
    "age":23,
    "work":"xyz",
    2:"Moja"
}
print(d.keys()) #(['name', 'age', 'work', 2])
print(d.values()) #(['Hejbulla', 23, 'xyz', 'Moja'])
print(d.items()) #([('name', 'Hejbulla'), ('age', 23), ('work', 'xyz'), (2, 'Moja')])

#replace values
print(d["age"]) #23
d["age"] = 33
print(d["age"]) #33
print(d) #{'name': 'Hejbulla', 'age': 33, 'work': 'xyz', 2: 'Moja'}

#add element
d["city"] = "Gazipur"
d["Country"] = "Bangladesh"
print(d) #{'name': 'Hejbulla', 'age': 33, 'work': 'xyz', 2: 'Moja', 'city': 'Gazipur', 'Country': 'Bangladesh'}

#also add element by using "update()"
d.update({"School":"BUSH", "Clg":"GCC"})
print(d) #{'name': 'Hejbulla', 'age': 33, 'work': 'xyz', 2: 'Moja', 'city': 'Gazipur', 'Country': 'Bangladesh', 'School': 'BUSH', 'Clg': 'GCC'}


#Pop element
d.popitem()
print(d) #{'name': 'Hejbulla', 'age': 33, 'work': 'xyz', 2: 'Moja', 'city': 'Gazipur', 'Country': 'Bangladesh', 'School': 'BUSH'}
#it just remove the last item

d.pop("age")
print(d) #{'name': 'Hejbulla', 'work': 'xyz', 2: 'Moja', 'city': 'Gazipur', 'Country': 'Bangladesh', 'School': 'BUSH'}
#remove specific element(age with value)


#If there are same key, then value take from last key
d = {
    "name":"Hejbulla",
    "age":23,
    "work":"xyz",
    "name":"Asad"
}
print(d) #{'name': 'Asad', 'age': 23, 'work': 'xyz'}



##Structred Information
Student_info = {
    "Shovon" : {"roll":123, "city":"Dhaka", "age": 30},
    "Maria" : {"roll":234, "city":"Gazipur", "age": 19}
}
print(Student_info["Maria"]) #{'roll': 234, 'city': 'Gazipur', 'age': 19}
print(Student_info["Shovon"]["city"]) #Dhaka



###
r = {}
print(r) #empty dict
print(type(r)) #dict

#l = [] -> empty list
#t = () -> empty touple
#d = {} -> empty dictionary
#s = set() -> empty set




#Set characteristics
#Mutable -> Yes
#Duplicate -> value can be duplicate but not key
#Index -> No
#Order -> Yes