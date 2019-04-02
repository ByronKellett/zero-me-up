# ZeroMeUp

Zeroes files with Python. Intended to be quick, not secure. I wrote it a while back to help someone doing data validation as part of their IT coursework, and they wanted to test that their file opening method wouldn't break if they got a file that was all zeroes and contained none of the expected data. The script worked, their program didn't, and so they fixed it.

## Licence

Public Domain. Do whatever. No warranty, no guarantees.

## Setup Instructions

Really simple. Download the script. Run it with one argument: the file you want to zero. Be warned, it has been known to work.

	python zerome.py zerome.py

Will work with all text files, should work with most binary files. Be warned with bigger ones. Written for Python 2 and 3. Note that if you copy and paste the above demonstration it will zero out the script - probably, I've not tested it and for good reason.

## Future Plans

There are none as of yet, but this could make a useful library. 
