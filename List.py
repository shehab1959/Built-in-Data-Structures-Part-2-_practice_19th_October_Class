my_list = ["shehab", 2, 3.1416, True, [1,3], ["Sjej",'erre'], "ffff"]
print(type(my_list))
print(len(my_list)) #7


#Empty list
your_list = []
print(len(your_list)) #0


##Create list using range
mylist = list(range(1,5))
print(type(mylist))
print(mylist) #[1, 2, 3, 4]
print("Total lenth:", len(mylist)) #Total lenth: 4


###List indexing
fruits = ["apple","banana","mango","guava","cherry","lichi"]
#index       0        1        2      3        4       5
#position    1        2        3      4        5       6
print(fruits) #show all
print(fruits[0]) #apple
print(fruits[1]) #banana
print(fruits[5]) #lichi
print(fruits[-1]) #lichi
print(fruits[-6]) #apple




###List Methods

sports = ["cricket","football","Ludo"]
print(sports) #['cricket', 'football', 'Ludo']

#add element in last
sports.append("Tennis")
print(sports) #['cricket', 'football', 'Ludo', 'Tennis']

#add element in the middle
sports.insert(2,"WWE")
print(sports) #['cricket', 'football', 'WWE', 'Ludo', 'Tennis']

#delete last element
sports.pop()
print(sports) #['cricket', 'football', 'WWE', 'Ludo']

#delete from the specific index
sports.pop(2)
print(sports) #['cricket', 'football', 'Ludo']

#reverse
sports.reverse()
print(sports) #['Ludo', 'football', 'cricket']


#Replace/ Exchange specific item
sports = ['cricket', 'football', 'WWE',{"Bat","Flower",'Net'}, 'Ludo', 'Tennis']
#indexing    0           1         2             3                4        5
print(sports)
sports[3] = "Badminton"
print(sports) #['cricket', 'football', 'WWE', 'Badminton', 'Ludo', 'Tennis']



###Looping through List
numbers = [1,3,4,6,8]
squared_numbers = []

for i in numbers:
    print(i)
    squared_numbers.append(i**2)
print(squared_numbers) #[1, 9, 16, 36, 64]

#list comprehension (ager ta short form)
numbers = [1,3,4,6,8]
squared_numbers = [i**2 for i in numbers]
print(squared_numbers) #[1, 9, 16, 36, 64]


#Self Practice looping through list
num = [1087,1393,1187,1848,1959]
empty_list = []

for i in num:
    print(i)
    empty_list.append(i+10)
print(empty_list) #[1097, 1403, 1197, 1858, 1969]


#
num = [1000,1300,1100,1800,1900]
empty_list = [i+10 for i in num]
print(empty_list) #[1010, 1310, 1110, 1810, 1910]

empty_list.reverse()
print(empty_list) #[1910, 1810, 1110, 1310, 1010]


print("Here List slicing output will print:")
###List Slicing
fruits1 = ["Apple", "Banana", "Cherry","Orange","Mango"]
print(fruits1[3]) #Orange
print(fruits1[-1]) #Mango
print(fruits1[-3]) #Cherry

print(fruits1[0:3]) #['Apple', 'Banana', 'Cherry']
print(fruits1[:3]) #['Apple', 'Banana', 'Cherry']
print(fruits1[1:]) #['Banana', 'Cherry', 'Orange', 'Mango']
print(fruits1[1:4]) #['Banana', 'Cherry', 'Orange']
print(fruits1[-5:-3]) #['Apple', 'Banana']

print(fruits1[0:5:2]) #['Apple', 'Cherry', 'Mango']
print(fruits1[::-1]) #['Mango', 'Orange', 'Cherry', 'Banana', 'Apple'] (reverse)