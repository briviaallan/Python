print("whatsup Nerdy peuple (:")
# A function is a block of code that only runs when it get called.

# Defining a Function#
# WE USE "def" and add a parentheses after and a collon.
def Odunga(mood = 'happy'): #the "mood" is the parameter. It is a vaiable that gets defined within the variable itself
    print(mood)
    if mood == 'happy':
        print('\nYeeY\n')
    else:
        print('\nAwww')
        
Odunga('happy') #tyiping this calls the finction to execute the parameters within the function
#If there is a default parameter value to the function definition, Then that stays as the default value
print('the first one')
Odunga()
print('\nthe second time')
Odunga('sad')
#RETURN#
#returning data to the orogonal place to oroginal function.

def take_it(m):
    return m+1

y = take_it(5) #we expect it to return "6"
print(y)