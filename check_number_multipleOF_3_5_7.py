given_no=int(input("the number is"))

multiple_of_3=given_no % 3==0
multiple_of_5=given_no % 5==0
multiple_of_7=given_no % 7==0

if multiple_of_3 and multiple_of_5 and multiple_of_7:
    print(str(given_no) +  "is multiple of 3, 5, 7")
elif multiple_of_3 and multiple_of_5:
    print(str(given_no) +"is multiple of 3 and 5")
elif multiple_of_5 and multiple_of_7:
    print(str(given_no) + "  is multiple of 5 and 7")
elif multiple_of_7 and multiple_of_3:
    print(str(given_no) + "is multiple of 7 and 3")
elif multiple_of_3:
    print(str(given_no)+  "is multiple of 3")
elif multiple_of_5:
    print(str(given_no) + "is multiple of 5")
elif multiple_of_7:
    print(str(given_no) + "is multiple of 7")
else:
    print(str(given_no) + "is not a multiple of 3,  5, 7")