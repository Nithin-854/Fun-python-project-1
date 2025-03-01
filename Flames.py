q = input("Enter the first name: ")
w = input("Enter the second name: ")

l = []
z = []
x = ['F', 'L', 'A', 'M', 'E', 'S']


for i in q:
    l.append(i.upper())

for i in w:
    z.append(i.upper())


for i in l[:]:
    if i in z:
        l.remove(i)
        z.remove(i)


e = len(l) + len(z)


while len(x) > 1:
    r = (e % len(x)) - 1
    if r >= 0:
        right = x[r + 1:]
        left = x[:r]
        x = right + left
    else:
        x = x[:len(x) - 1]

print(f"The relationship is: {x[0]}")
