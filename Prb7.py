#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

a = input("Enter hours: ")
b = input("Enter rate: ")
hours = float(a)
rate = float(b)
pay = hours * rate
extra = 0
if hours > 40:
    extra = (hours - 40) * (rate * 1.5)
totalpay = pay + extra
print("Pay of employee: ",totalpay)
