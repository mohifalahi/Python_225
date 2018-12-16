# password generator
import random
n = 3
l = ""
for i in range(n):
    l = l + chr(random.randint(97,122))
u = ""
for i in range(n):
    u = u + chr(random.randint(65,90))
d = ""
for i in range(n):
    d = d + str(random.randint(1,9))
print(l + u + d)
