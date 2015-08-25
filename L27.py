__author__ = 'Hernan Y.Ke'
import subprocess
proc = subprocess.Popen(['echo','hello'],stdout=subprocess.PIPE)
out,err = proc.communicate()
print(out.decode('utf-8'))