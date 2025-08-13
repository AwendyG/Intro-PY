# Tuples
# Store data of any kind including int, str, char
# Not editable
# Defined by normal brackets ()
# They are ordered "indexed"

my_tuple = ("apple", "banana", "orange", "lemon")

print(my_tuple[2])

#we can use s comma to creat a tuple
tuple = (5,)
print(type(tuple))

#we can add or mutiply tuples

t1 = (1,2)
t2 = (3,4)

print(t1+t2)
print(t2 * 4)

#we can count how many times an element is in the tuple
my_tuple = ("girl", "boy", "girl", "boy")
print(my_tuple.count("girl"))

