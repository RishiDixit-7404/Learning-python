z = 10
def our_print(s):
    print(f"the print is {s}")
    print(z)
    
our_print("hi ")

def time_times2(x):
    return x*2
print(time_times2(10))

def append_4_to_list(lst):
    lst.append(4)
    print(lst)
a = [1,2,3]
append_4_to_list(a)
print(a)

def update(x):
    x+=1
    print(x)
b = 10
update(b)
print(b)
def add(a,b,c=2):
    return a + b + c
print(add(10,12))
