def new_line_separator():
    with open ('/home/vladi/Education/GB/Python/HelloyPython/my/S7/telephone_directory/select_rec_format', 'r') as data:
        for i in data:
            if i == "1":
                return " /"
            else:
                return 2 * " /"
