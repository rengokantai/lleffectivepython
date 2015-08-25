__author__ = 'Hernan Y.Ke'
from collections import defaultdict

def log_missing():
    print ('key added')
    return 0

#d = defaultdict(lambda  :100)
d = defaultdict(log_missing)
d['foo']= 55
print(d['foo'])
print(d['bar'])
