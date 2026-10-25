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


#No indexing
"""
s = {1,2,35,5,4,3}
print(s[1]) #error

s = {"apple","banana","cherry"}
print(s[0]) #error

"""


###Set Methods

#add element
s = {"apple","banana","cherry"}
s.add("mango")
print(s)


my_set = {"apple", "banana"}
my_set.add("cherry")
print(my_set)  # Output: {'banana', 'cherry', 'apple'} (Note: sets are unordered)

# Trying to add a duplicate has no effect
my_set.add("apple")
print(my_set)  # Output: {'banana', 'cherry', 'apple'}

#remove element (remove if element available, if not available then show error)
s = {"apple","banana","cherry"}
s.remove("apple")
print(s) #{'cherry', 'banana'}

#s.remove("cricket")
#print(s) #error

#discard element (if element are not available on set that we want to remove and try to avoid error then we have to use it)
s = {"apple","banana","cherry"}
s.discard("cricket")
print(s) #show only element {'apple', 'cherry', 'banana'}, there is no error show






###
old_subscriber = {"rafia1@gmail.com","sarif10@gmail.com","sadia101@gmail.com","hasan111@gmail.com"}
new_subscriber = {"sadia101@gmail.com","hasan111@gmail.com","sayem201@gmail.com","adnan211@gmail.com"}

#total indivisual unique subscriber:
total_unique = old_subscriber.union(new_subscriber)
print(total_unique) #6 {'sayem201@gmail.com', 'sarif10@gmail.com', 'hasan111@gmail.com', 'rafia1@gmail.com', 'adnan211@gmail.com', 'sadia101@gmail.com'}

#common subscriber:
loyal = old_subscriber.intersection(new_subscriber)
print(loyal) #2 {'sadia101@gmail.com', 'hasan111@gmail.com'}

#Only old subscriber, jara new subscriber na
only_old = old_subscriber.difference(new_subscriber)
print(only_old) #2 {'rafia1@gmail.com', 'sarif10@gmail.com'}

#Only new subscriber, jara old subscriber na
only_new = new_subscriber.difference(old_subscriber)
print(only_new) #2 {'sayem201@gmail.com', 'adnan211@gmail.com'}





#Set characteristics
#Mutable -> Yes
#Duplicate -> No
#Index -> No
#Order -> No