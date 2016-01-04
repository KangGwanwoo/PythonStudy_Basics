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
		end_char = '\n' if count % per_line == 0 else '\t'

		print(year, end=end_char)
		
		year += step

		count += 1

if __name__ == '__main__':main()