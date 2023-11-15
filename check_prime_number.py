num=int(input("enter the number--"))

if num == 1:
    print("it isn't a prime number")

if num > 1:
    for i in range(2, num):
        if num % i ==0:
            print("it isn't a prime number")
            break
        else:
            print("it is a prime number")
            break