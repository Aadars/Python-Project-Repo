from collections import Counter
s='asadsafafdf'
s = Counter(s)
print(s.values())

##-------------- NEXT ---------------------------##

s='asadsafafdf'
s = Counter(s)
print(s.clear())

##-------------- NEXT ---------------------------##

s='asadsafafdf'
c = Counter(s)
print(list(c))

##-------------- NEXT ---------------------------##

s='asadsafafdf'
c = Counter(s)
print(set(c))


##-------------- NEXT ---------------------------##

s='asadsafafdf'
c = Counter(s)
print(dict(c))

##-------------- NEXT ---------------------------##

s='asadsafafdf'
c = Counter(s)
print(c.items())


##-------------- NEXT ---------------------------##

s='asadsafafdf'
c = Counter(s)
print(dict(c.items()))

##-------------- NEXT ---------------------------##

s=[1,2,3,4,5,6,7,89,0,0,0,1,2,1,2,3,2,1,5,6,4,3,5,6,67,4]
c = Counter(s)
print(dict(c))

##-------------- NEXT ---------------------------##

s='asadsafafdf'
c += Counter(s)
print(c)

##-------------- DEFAULT DICT ---------------------------##

from collections import defaultdict
d={}

d = defaultdict(object)
print(d['one'])
for item in d:
    print(item)

##-------------- NEXT ---------------------------##



##-------------- NEXT ---------------------------##
from collections import namedtuple 
sam = namedtuple('Dog','name breed age')
obj1 = sam(name='sam',breed='lab',age=2)
print(obj1)


##---------------------------------NEXT ---------------------------##
