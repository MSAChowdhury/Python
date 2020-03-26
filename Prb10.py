#import to call some header file
import random
for i in range(10):
    x = random.random() # . random will pick randomly from .00 to 1.00
    print(x)
    y = random.randint(3, 8) # . ranint will chose one from low and high
    print(y)
    str = [1, 43, 6, 53,0]
    z = random.choice(str) # . choice will choose one elements from array
    print(z)
