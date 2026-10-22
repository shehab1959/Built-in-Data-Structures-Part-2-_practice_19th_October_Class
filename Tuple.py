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




### Tuple Unpacking
t = ("hello", 'world', 13)
print(t) #('hello', 'world', 13)

#
a,b,c=t
print(t) #('hello', 'world', 13)

#
t3 = ("hejbulla","asad",1959)
a = t3[0]
b = t3[1]
c = t3[2]
print(a,c,b) #hejbulla 1959 asad

#
t5 = ("hello", 'world', 13)
print(t5) #('hello', 'world', 13)
a,b,c = t5
print(a) #hello
#print(d) #error

#
t5 = ("Hello","World",13,3.14,27)
print(len(t5)) #5

a,b,*c = t5
print(a,b,c) #Hello World [13, 3.14, 27]

*a,b,c = t5
print(a,b,c) #['Hello', 'World', 13] 3.14 27

a,*b,c = t5
print(a,b,c) #Hello ['World', 13, 3.14] 27


##Tuple methods (2 types)
t7 =(1,2,2,3,2,4,3,5)

#1.Count()
print(t7.count(3)) #2 (3 ache total 2 bar)
print(t7.count(2)) #3 (2 ache total 3 bar)

#2.index()
print(t7.index(4)) #5 (value 4 ache 5 number index e)
print(t7.index(1)) #0 (value 1 ache 0 number index e)
print(t7.index(2)) #1 (value 2 ache 1 number index e)





##Tuple are:
#Immutable
#Indexing->Yes
#Duplicate item -> Yes
#Ordered -> Yes