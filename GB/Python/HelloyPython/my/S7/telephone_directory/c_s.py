def character_separator():
    with open ('/home/vladi/Education/GB/Python/HelloyPython/my/S7/telephone_directory/select_rec_format', 'r') as data:
        for i in data:
            if i == "2":
                return ";"
            else:
                return " /"
