import sys
import os

# Gets size of the file via two different methods.
x = os.stat(sys.argv[1]).st_size
y = os.path.getsize(sys.argv[1])

# Opens file for writing
f = open(sys.argv[1], "wb")
# By default, size method 1 is chosen for use later
z = x
# Is file size calculation method 2 is bigger, its result is used later instead.
if y > z:
	z = y


s = b'\0'
t = s
# For every byte in the file, a zero is created. Therefore, a chunk of zeroes is stored in memory. Not the most effecient way, but it doesn't really matter much. It now also accounts for the t string already having 1 byte of data, meaning it shouldn't make the file bigger (something I noticed was occuring in testing).
for i in range(z-1):
	t = t + s	

# Writes file and finishes
f.write(t)
f.close()

