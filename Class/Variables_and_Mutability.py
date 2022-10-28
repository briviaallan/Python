# variables can be assigned to any data type
###############################
# There are Rules!
#1 Has to start with an Alphabetical character of an underscore.
Allan = 'Subcribe'
#2 Variables are case sensitive
Brivia = "awsome"
brivia = 'lame'
#3 Variables can only contain Alphanumeric characters and underscores. No "$, @, !, #, %, ^, * "
################################
##########Mutability#############
# Immutable > these variables can not be changed e.g Tuple
# Mutable > THese variables can be changed e.g Lists

#Muttable
s = [1, 2, 3]
#changing any item, means you index into the list to change the value.
s[1] = 5 #The 1th position "2" has been changed to "5"

#Immutable
t = (1, 2, 3)
t[1] = 5 # t will be impossible to change the 1th inex since this is a tuple. but:
# we can change it by re-writing the whole tuple.
t = (1, 5, 3)
#the same is also the case for a string.
string = 'string'
string = string + 's' #Here, we're creating a new value in memory and we're moving the pointer to reasign the original string variable name to the new value "strings"
# in short hand:
string += 's'
###########
x = 1
x += 1
