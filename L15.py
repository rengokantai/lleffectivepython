__author__ = 'Hernan Y.Ke'
numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}

def helper(x):
    if x in group:
        return (0,x)        #0, 1 means priority group
    return (1,x)

numbers.sort(key=helper)
print(numbers)