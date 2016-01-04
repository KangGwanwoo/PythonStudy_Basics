#!/usr/bin/env python3
#

def print_years1(start_year, end_year, step=1,per_line=10):

	if start_year >= end_year:
		print("Invalid start ({start}) and end ({end}) years !".format(start=start,end=end_year))
		return

	count = 1
	for year in range(start_year,end_year+1,step):
		end_char = "\n" if count % per_line == 0 else "\t"
		print(year, end=end_char)
		count += 1

	print("\n\n{num} years printed.".format(num=count-1))


def print_years2(start_year,end_year,step=1,per_line=10):

	if start_year >= end_year:
		print("Invalid start ({start}) and end ({end}) years !".format(start=start,end=end_year))
		return

	years = range(start_year,end_year+1,step)

	years_to_print = [str(y) + "\n" if years.index(y)+1 % per_line == 0 else str(y)+"\t" for y in years]

	print(" ".join(years_to_print))

	print("\n\n{num} years printed.".format(num=len(years_to_print)))


def main():
	print("\n\n Print Years Vesion 1")
	print_years1(1800,2014,2,10)
	print("\n\n Print Years Vesion 2")
	print_years2(1800,2014,2,10)

if __name__ == '__main__':
	main()

