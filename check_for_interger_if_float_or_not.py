num=input("enter anything--")

def float_chek(num):
    try:
        float(num)
        return True
    except:
        return False

print(float_chek(num))
