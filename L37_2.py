__author__ = 'Hernan Y.Ke'
import gc
import L37
import tracemalloc


found_objects =gc.get_objects()
print('%d object before' % len(found_objects))

x = L37.run()
found_objects =gc.get_objects()
print('%d object after' % len(found_objects))

for obj in found_objects[:3]:
    print(repr(obj)[:100])

tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()
x = L37.run()
time2 = tracemalloc.take_snapshot()
stats = time2.compare_to(time1,'lineno')

for stat in stats[:3]:
    print(stat)

stats = time2.compare_to(time1,'traceback')
top = stats[0]
print('\n'.join(top.traceback.format()))
