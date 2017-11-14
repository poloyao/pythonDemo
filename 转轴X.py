
import sys, time

for i in range(1000): 
    sys.stdout.write('|'+'\r') 
    time.sleep(0.05)
    sys.stdout.write('/' +'\r') 
    time.sleep(0.05)
    sys.stdout.write('-' +'\r') 
    time.sleep(0.05)
    sys.stdout.write('\\' +'\r') 
    time.sleep(0.05)