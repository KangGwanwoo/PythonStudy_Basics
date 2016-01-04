#!/usr/bin/env python3

def print_year(start,end,step=1,per_line=10):
	year = start
	count = 1
	for year in range(start, end+1):
		end_char = "\n" if count % per_line == 0 else "\t"
		print(year,end=end_char)

		year += step
		count += 1


def main():
	"""program entry point
	"""
	print_year(1800,2014,step=3,per_line=5)

if __name__ == '__main__':
	main()