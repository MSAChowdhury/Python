str = 'X-DSPAM-Confidence:0.8475'
a = str.find(":")
print(a)
b = len(str)
print(b)
res = str[(a+1):(b-1)]
print(res)
num = float(res)
print("Floating Number: ",num)