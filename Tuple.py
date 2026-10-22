my_tuple = (1,2,7) #(1, 2, 7)
print(my_tuple)
print(type(my_tuple))

t = ("Hello",1,4,True,4.37,[1,3],(4,5,6),"world")
print(len(t)) #8


#Create tuple using range function
print(tuple(range(1,20,2))) #(1, 3, 5, 7, 9, 11, 13, 15, 17, 19)


##
tt = ("Hello","World",3.1416)
print(tt[1]) #World
print(tt[-1]) #3.1416
print(tt[::-1]) #(3.1416, 'World', 'Hello')
print(tt[0:3:2]) #('Hello', 3.1416)

#The indexing and slicing are same for both tuple and list