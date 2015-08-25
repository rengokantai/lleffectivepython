__author__ = 'Hernan Y.Ke'

a = [1, 2, 3, 4, 5]

squares = map(lambda x: x**2, a)
print(list(squares))
#alt = x**2 for x in a if x%2==0 better!
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
print(list(alt))