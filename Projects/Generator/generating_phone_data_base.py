import random

print('Hallow World')

def Generator(x):
    z = input((f'want a number? (1)yes, (2),no: '))
    Feedback = ''

    if z == '1':
        Random_Phone = random.randint(10000000000, x)
        Random_Phone = Random_Phone + 1
        phone = Random_Phone
        if phone >= 10000000000 and phone <= 999999999999:
            print(phone,'here is your phone: ')
        elif phone < 10000000000 and phone > 999999999999:
            print(' Lemme Try again')
        while phone == Random_Phone:
            feedback = input(f'want another number? (y) for Yes, (n) for No: ')
            if feedback == 'y':
                print(phone, 'here is another')
            else:
                print('Nice knowing ya!')
                break
    
        

Generator(999999999999)