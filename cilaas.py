class human:
    def __init__(self, age, name):
        self._age = age
        self._name = name
    def __str__(self):
        return 'name is '+ self._name+' age is '+ str(self._age)
    def old_younge_than(self, age):
        if self._age>age:
            print('no')
        elif self._age<age:
            print('yes')
    
h = human(age=4, name = "ris")
print(h)
print(h._name)
print(h.__str__())
h.old_younge_than(12)
