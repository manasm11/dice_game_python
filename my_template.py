
def check_str(value): assert isinstance(value, str), f"{value} is not a string"
def check_int(value): assert isinstance(value, int), f"{value} is not an int"
def check_bool(value): assert isinstance(value, bool), f"{value} is not an bool"
def check_list(value): assert isinstance(value, list), f"{value} is not a list"
def check_dict(value): assert isinstance(value, dict), f"{value} is not a dict"
def check_in(value, list_): assert value in list_, f"{value} is not in {list_}"
def clear_screen():print(chr(27) + "[2J")
