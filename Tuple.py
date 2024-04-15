#Task 1 modification tuple
#Given Data
tup = (10, 20, 30, 40, 50)

# Adding 60 to the tuple
tup = tup + (60,)
print( tup)

# Removing 50 from the tuple
t = (10, 20, 30, 40, 50, 60)
new_t = tuple(x for x in t if x != 50)
print(new_t) 

# Replacing an element in the tuple
tup = tuple(list(tup)[:4] + [50] + list(tup)[5:])
print(tup)

tup = tup[:-1]
print(tup)
