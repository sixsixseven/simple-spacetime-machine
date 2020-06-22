#	Python 3; Written by github.com/sixsixseven, the world's first fully-autonomous underwater coputer programmer.
import time
import random

year = str(input("Please input a destination year: "))
month = str(input("Please input a destination month: "))
day = str(input("Please input a destination day: "))

print("Transporting... Please close your eyes and make wibbly-wobbly timey-wimey sounds.")
time.sleep(random.randrange(3,17))

print("""\n\n\n
Welcome Spacetime Traveler!

The current date is:

	%s-%s-%s
""" % (year,month,day))
