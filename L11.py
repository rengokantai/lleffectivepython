__author__ = 'Hernan Y.Ke'
li = ['aa','bbd','dsf']

#li = [2,3,4]
itera = (len(x) for x in li)
roots =((x, x**0.5) for x in itera)

while True:
    try:
        print(next(roots))
    except StopIteration:
       exit(0)
