#!/usr/bin/env python3

def main():
	"""program entry point
	"""

	start = 1800
	end = 2014
	step = 2
	per_line = 10

	year = start
	count = 1

	while year <= end:
		if count % per_line == 0:
			print(year, end='\n')
		else:
			print(year, end='\t')

		year += step

		count += 1

if __name__ == '__main__':main()