i=3
j=0
for row in range(4):
    for col in range(7):
        if col==0 or col==6 or (col==4 and row ==1) or (col==5 and row== 2):
            print("*", end="")
        elif row==j and col==i:
            print("*", end="")
            j=j+1
            i=i-1
        else:
            print(end=" ")
    print()