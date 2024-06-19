#!/usr/bin/python3

import re

def email_validator(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat, s):
        return True
    else:
        return False