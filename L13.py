__author__ = 'Hernan Y.Ke'


def normalize(get_iter):

    results=[]
    total = sum(get_iter())
    for elem in get_iter():
        results.append(100 * elem/total)
    return results

path = '/L13.txt'
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


get_iter = lambda : read_visits('./L13.txt')

print(normalize(get_iter))

class ReadV(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(path) as f:
            for line in f:
                yield int(line)


visits = ReadV('./L13.txt')
it = iter(visits)
it2 = iter(visits)
print(it, it2)