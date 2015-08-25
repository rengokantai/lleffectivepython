__author__ = 'Hernan Y.Ke'
#multithread
import time
import threading
def factorize(number):
    for i in range(1,number+1):
        if number % i == 0:
            yield i

numbers = [1234,3244,4213,3422]

class Factorize(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number
    def run(self):
        self.factors = list(factorize(self.number))
start = time.time()
threads=[]
for number in numbers:
    thread = Factorize(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    print("factors: %r" % thread.factors)
end = time.time()
print("time was %.3f" % (end-start))
# thread = Factorize(21)
# thread.start()
# thread.join()
# print(thread.factors)