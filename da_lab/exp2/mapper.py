#!/usr/bin/env python3
# import sys because we need to read and write data to STDIN and STDOUT
#!/usr/bin/python3
import sys
for line in sys.stdin:
	line = line.strip() # remove leading and trailing whitespace
	words = line.split() # split the line into words
	for word in words:
		print( '%s\t%s' % (word, 1))
