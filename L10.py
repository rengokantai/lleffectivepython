__author__ = 'Hernan Y.Ke'
matrix = [[1,2,3],[4,5,6],[7,8,9]]

#must use bracket
filtered = [[x for x in row if x % 3 ==0] for row in matrix if sum(row)>=10]

print(filtered)