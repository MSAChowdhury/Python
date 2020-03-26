# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(h, r):
    try:
        hours = float(h)
    except:
        print("Error, please enter numeric input")
    try:
        rate = float(r)
    except:
        print("Error, please enter numeric input")
    pay = hours * rate
    extra = 0
    if hours > 40:
        extra = (hours - 40) * (rate * 1.5)
    totalpay = pay + extra
    return totalpay

a = input("Enter hours: ")
b = input("Enter rate: ")
print("Pay of employee: ",computepay(a,b))
