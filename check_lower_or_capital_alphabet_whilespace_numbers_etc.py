input=input("input by user--")

if input.islower():
    print("the given input is in lower case")
elif input.isupper():
    print("the given input is in upper case")
elif input.isspace():
    print(" the given character is white space")
else:
    print("type value input")