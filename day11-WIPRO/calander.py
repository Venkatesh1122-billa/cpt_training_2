# from calendar import *
# year = int(input("Enter a year number: "))
# Month = int(input("Enter a month number: "))
# str = month(year,Month)
# print(str)




from calendar import *
year = int(input("Enter a year number: "))
if isleap(year):
    print(year, "is leap year")
else:
    print(year , "is not a leap year")


'''program to print the next 10 days dates continuously '''

from datetime import *
d  = date.today()
print(d)
d  = date(1996, 6, 1)
for x in range(1,10):
    nextdate = d+timedelta(days=x)
    print(nextdate)

import time
epoch = time.time()
print(epoch)