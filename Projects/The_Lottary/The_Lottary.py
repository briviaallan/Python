from ast import ListComp
import random
from xml.dom import xmlbuilder
print('Hallo_World!\n')
print('try this one\n')

def Boder_line(x):
    Lottary = random.randint(2, x)
    your_number = 0
    while your_number != Lottary:
        your_number = int(input(f'Write your winning number between 2 and {x}:'))
        if your_number < Lottary:
            print("Sorry, (; Better Luck Next Time")
        elif your_number > Lottary:
            print("Sorry, (; Better Luck Next Time")
        if your_number == Lottary:
            print('Yay!!! You Won!')
            break
    return(Lottary)
Boder_line(5)

def LeaveYourNumber(x):
    j = 3
    print('Phone Number')
    phone_Number = int(input(f'Input your phone number: '))
    while j == 3: #phone_Number <= 999999999999
        phone_Number = int(input(f'confirm your number: '))
        if phone_Number > 999999999999:
            int(input(f'Input the correct number format')) #and phone_Number <= 999999999999:
        elif phone_Number <= 999999999999 and phone_Number > 99999999999:
            print('Thank You\n')
            print('We will contact you shortly')
            break

LeaveYourNumber(999999999999)