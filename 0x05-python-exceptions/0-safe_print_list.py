#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	for i in range(x):
		count = 0
		try:
			print("{:d}".format(i), end="")
		except IndexError:
			continue
		count += 1
	return count
