__author__ = 'Hernan Y.Ke'
import select
import time
def slow_syscall():
    select.select([],[],[],0.1)

start = time.time()
for _ in range(5):
    slow_syscall()
end = time.time()


print("time was %.3f" % (end-start))