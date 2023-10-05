input=str(input("input by user--"))

if input ==input[::-1]:                #In Python, [::-1] is a slicing technique used to reverse a sequence (such as a string, list, or tuple).
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")