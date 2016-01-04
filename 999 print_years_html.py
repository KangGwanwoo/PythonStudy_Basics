#!/usr/bin/env python3
#

def print_header():
	return "<html><body>\n<table border=1>\n"

def print_footer():
	return "\n</table>\n</body></html>"

def print_years(start_year, end_year, step=1,per_line=10):

	assert start_year < end_year, "Invalid start ({start}) and end ({end}) years !".format(start=start,end=end_year)

	lines = []
	count = 1

	for year in range(start_year,end_year+1,step):
		start_tag = "\n<tr><td>" if count % per_line == 1 else "<td>"
		end_tag = "</tr></td>\n" if count % per_line == 0 else "</td>"

		lines.append(start_tag+str(year)+end_tag)
		count += 1

	for _ in range((count-1) % per_line, per_line):
		lines.append("<td>&nbsp</td>")
	lines.append("</tr>\n")

	return "".join(lines)

def main():
	with open('./years.html','w') as f:
		print(print_header(),file=f)
		print(print_years(1,2014,3,10),file=f)
		print(print_footer(),file=f)

if __name__ == '__main__':
	main()

