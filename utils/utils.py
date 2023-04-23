import re

def find_info(look_for, text):
    if re.search(look_for,text):
	    return True
    else:
        return False