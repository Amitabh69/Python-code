num=int(input(" enter four digit number is-"))

if num<=1000 or num<=9999:
    thousand_place=num//1000 # // operator divides the first number by the second number
                             # and rounds the result down to the nearest integer (or whole number)
    hundred_place=(num//100)%10
    tenth_place=(num//10)%10
    ones_place=num%10

    print("number at thousand place="+ str(thousand_place))
    print("number at hundered place="+ str(hundred_place))
    print("number at tenth place="+ str(tenth_place))
    print("number at ones place="+ str(ones_place))
else:
    print("input valid four digit number!")
