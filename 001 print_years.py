#!/usr/bin/env python3
#

def main():
	"""program entry point
	"""

	start = 1800
	end = 2014

	year = start

	while year <= end:
		print(year, end='\t')
		year += 1

	print("\n")

if __name__=='__main__':main()
