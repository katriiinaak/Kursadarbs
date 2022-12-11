"""
import random

x = random.randint(0,10)
y = 7
while x != y:
    print(x)
#

stop_at = 7
while True:
    num = random.randint(0, 10)
    if num == stop_at:
        break
    print(num)
#

from itertools import starmap, repeat, takewhile
from random import randint

for num in takewhile(lambda L: L != 7, starmap(randint, repeat( (0, 10) ))):
    print(num)
#
"""

import random

x = random.randint(0,8)
y = 7
while x != y:
    print(x)   #Print old (non-7) random number
    x = random.randint(0,8)  #pick a new number.  I hope it's 7 so we can end this madness

print("You found {0}.  Congrats.  Go have a beer.".format(y))