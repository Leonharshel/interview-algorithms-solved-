import math  # to use factorial method

l1 = []
l2 = []
l3 = []
a = input('type the bucket id: ')
for i in a:
    b = int(i)
    l1.append(b)

# function to calculate permutation of 2 digits


def perm(n, r):
    p = math.factorial(n) / math.factorial(n-r)
    return p


for x in l1:
    for y in l1:
        if(x > y):
            c = perm(x, y)
            l2.append(c)
d = (max(l2))
print("the integer representing the bucket id is ", d)
