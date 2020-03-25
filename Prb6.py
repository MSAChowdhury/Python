n = input("Press '1' to find Temperate in Celsius\n//\nPress '2' to find Temperate in Farenheit\n: ")
if int(n) == 1:
    farenheit = input("Enter the temperature in Farenheit: ")
    celsius = float(farenheit) - 32 * (9/5)
    print("The temperature in Celsius is: %.2f" % round(celsius,2))
else:
    celsius = input("Enter the temperature in Celsius: ")
    farenheit = float(celsius) * (5/9) + 32
    print("The temperature in Farenheit is: {0:.2f}".format(farenheit))
# to have precision after decimal point in python, there are types: ("%.2f" % variable) or ("%.2f" % round(celsius,2)) or "{0:.2f}".format(farenheit) or "{0:.2f}".format(round(farenheit,2))
