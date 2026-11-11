# built a code which wish you good morning, good afternoon and good night based on the time of the day
import time
timestamp=int(time.strftime("%H"))
if timestamp<12:
    print("good morning")
elif timestamp<16:
    print("good afternoon")
elif timestamp<20:
    print("good evening")
else:
    print("good night")