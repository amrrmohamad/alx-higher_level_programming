#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""


from sys import argv
from os.path import exists

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

namefile = "add_item.json"
argc = len(argv)

file_list = []

if exists(namefile):
    file_list = load_from_json_file(namefile)

if (argc == 1):
    save_to_json_file(file_list, namefile)
else:
    for index in range(1, argc):
        file_list.append(argv[index])
    save_to_json_file(file_list, namefile)
