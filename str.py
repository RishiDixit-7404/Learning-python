num = '20'
name = 'rishi'
n = f'hi {name} how is it going today, you are {num} years old'
print(n)
n = 'hi {0} how is it going today, you are {1} years old'.format(name,num)

print(sorted(set(n)))
for i in name:
    print(i)

n2= n.split(" ")
print(n2)
print(type(n2))
print(name.isnumeric())
print(num.isnumeric())
n3=n.upper()
print(n3)


