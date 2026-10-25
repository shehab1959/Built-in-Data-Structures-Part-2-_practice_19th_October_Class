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







###
r = {}
print(r) #empty dict
print(type(r)) #dict

#l = [] -> empty list
#t = () -> empty touple
#d = {} -> empty dictionary
#s = set() -> empty set