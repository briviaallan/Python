###While Loop

Brivia = 300

while Brivia < 500:
    print(Brivia)
    Brivia = Brivia + 25
print("the end")


### For Loop
name = "Brivia"
for x in name:
    print(x)

### For Loop in a List
N = ['Brivia', 'is', 'awsome']
for K in N:
    print(K)

### Nested For Loop
# a list of stuff
cartoons = ['eddy, ed, and, edde,', 'garfield,', 'chowder,']
movies = ['the flash', 'the watchers', 'batman']

for toons in cartoons:
    for movers in movies:
        print(toons, movers)


#### CONTROL FLOW STATEMENTS####
# Break#
for K in N:
    print(K)
    if K == 'is':
        break
print('Yay! That was fun')

#Continue#
for K in N:
    if K == 'is':
        continue
    print(K)
print('Yay! That was fun')