import sys
import time


i = int(sys.argv[1])

while i > 0 :
    print(i)
    time.sleep(0.5)
    i -= 1

print("BOOM!")