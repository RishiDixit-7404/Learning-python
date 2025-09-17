from copy import deepcopy
a = list(range(0,10))
print(a)
b = deepcopy(a)
print(b)
b.append(10)
print(b)
print(a)