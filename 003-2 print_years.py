#!/usr/bin/env python3

def main():
	"""program entry point
	"""

	start = 1800
	end = 2014
	step = 1
	per_line = 10

	year = start
	count = 1

	for year in range(start,end-1):
		end_char = ""
		if count % per_line == 0:
			end_char = "\n"
		else:
			end_char = "\t"

		count += 1

		print(year,end = end_char)

if __name__ == '__main__':
	main()