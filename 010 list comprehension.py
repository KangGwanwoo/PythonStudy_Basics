#!/usr/bin/env python3

def main():
	"""program entry point
	"""
	
	years_to_print = [str(y) for y in range(1800,2014,1)]

	print(years_to_print)
	print("\n\t")
	print(" ".join(years_to_print))
	print("=".join(years_to_print))
	print("\t".join(years_to_print))

if __name__ == '__main__':
	main()