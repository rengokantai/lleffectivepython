__author__ = 'Hernan Y.Ke'
#single thread
import time
def factorize(number):
    for i in range(1,number+1):
        if number % i == 0:
            yield i

numbers = [1234,3244,4213,3422]

start = time.time()
for number in numbers:
    list(factorize(number))
end = time.time()
print("time was %.3f" % (end-start))