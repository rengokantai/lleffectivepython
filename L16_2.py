__author__ = 'Hernan Y.Ke'
from collections import defaultdict

class CountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self, *args, **kwargs):
        self.added +=1
        return 0

counter = CountMissing()    #Call new instance for __call__
current = {'green':12, 'blue':3}
result = defaultdict(counter, current) #first param is a hook function, second is default dict
increments = [('red',5),('blue',2),('green',12)]

for key,offset in increments:
    result [key]=offset

print(counter.added)
