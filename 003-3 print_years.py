#!/usr/bin/env python3

def my_year_range(start,end,step=2):
	"""
		iterator should yield resulting value
	"""
	result = start
	while result < end:
		yield result
		result += step

def main():
	"""program entry point
	"""

	start = 1800
	end = 2014
	step = 2
	per_line = 10
	year = start
	count = 1


	for year in my_year_range(start,end-1):
		end_char = ""
		if count % per_line == 0:
			end_char = "\n"
		else:
			end_char = "\t"

		count += 1

		print(year,end = end_char)

if __name__ == '__main__':
	main()