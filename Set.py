##Set (only show unique value)
s = {1,2,3,4,3}
print(type(s))
print(s) #{1, 2, 3, 4} #3 print only one time as set always print unique value



##Create set using range
# Creates a set of numbers from 0 to 4
my_set = set(range(5))
print(my_set) #Output: {0, 1, 2, 3, 4}

# Creates a set with custom start and stop values (3 to 7)
custom_set = set(range(3, 8))
print(custom_set) #Output: {3, 4, 5, 6, 7}



#Set er vitor list/set rakha jayna
#s = {1,2,3,[11,12]}
#print(s) #Error


#No order maintain
ss = {"apple","banana","cherry"}
print(ss) #{'cherry', 'apple', 'banana'}

sss = {2,3,1,4}
print(sss) #{1, 2, 3, 4}