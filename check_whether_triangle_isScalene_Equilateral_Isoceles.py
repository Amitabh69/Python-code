side1=int(input("side1_is-"))
side2=int(input("side2_is-"))
side3=int(input("side3_is-"))

if side1==side2==side3:
    print('It is an equilateral triangle')
elif side1==side2 or side1==side3 or side2==side3:
    print('It is an Isoceles triangle')
else:
    print('It is an Scalene triangle')
