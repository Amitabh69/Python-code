#                  RANDOM PASSWORD GENERATOR

#REQUIREMNTS-- RANDOM MODULE, CHARACTER-LOWER, UPPER, NUMBER, SYMBOL
# LENGTH OF PASSWORD AND COUNT OF PASSWORD, NESTED FOR LOOP WILL BE USED FOR IT
#EMPTY STRING WILL BE REQUIRED TO STORE THE GENERATED PASSWORD
#WHILE TRUE WILL BE USED TO STOP ABOVE LOOP WITH BREAK.

import random
character="abcdefghijlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*"
while True:
    PASS_LENGTH=int(input("enter the length of required password"))
    pass_count=int(input("enter the number of password to be generated"))

    for i in range (0 , pass_count):
        password=" "
        for j in range(0,PASS_LENGTH):
            pass_charcter= random.choice(character)
            password=password+pass_charcter
        print("The generated password is-",password)
    repeat=input("Repeat generating password?")
    if repeat=="No" or repeat=="No":
        break
print("Thank you")

