# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully
#by printing a message and exiting the program. The following shows two executions of the program:
a = input("Enter hours: ")
b = input("Enter rate: ")
try:
    hours = float(a)
except:
    print("Error, please enter numeric input")
try:
    rate = float(b)
except:
    print("Error, please enter numeric input")
pay = hours * rate
extra = 0
if hours > 40:
    extra = (hours - 40) * (rate * 1.5)
totalpay = pay + extra
print("Pay of employee: ",totalpay)
