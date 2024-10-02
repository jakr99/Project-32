# Jacob Lee

import re

def is_integer(s):
    return re.match(r'^[-+]?[0-9]+$', s) is not None

def is_decimal(s):
    return re.match(r'^[-+]?[0-9]+\.[0-9]+$', s) is not None

def is_scientific(s):
    return re.match(r'^[-+]?[0-9]+\.[0-9]+E[-+]?[1-9][0-9]*$', s) is not None

def is_hexadecimal(s):
    return re.match(r'^[0-9A-F]+H$', s) is not None

def is_keyword(s):
    return s in ['DEF', 'IF', 'FI', 'LOOP', 'POOL', 'PRINT']

def is_string_literal(s):
    return re.match(r'^"[^ ]+"$', s) is not None

def is_character_literal(s):
    return re.match(r'^[0-9A-F]{2}X$', s) is not None

def is_identifier(s):
    return re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', s) is not None and not is_keyword(s)

def main():
    N = int(input())
    print(N)
    for i in range(N):
        s = input().strip()
        if is_integer(s):
            print(f"{i + 1}: Integer")
        elif is_decimal(s):
            print(f"{i + 1}: Decimal")
        elif is_scientific(s):
            print(f"{i + 1}: Scientific")
        elif is_hexadecimal(s):
            print(f"{i + 1}: Hexadecimal")
        elif is_keyword(s):
            print(f"{i + 1}: Keyword")
        elif is_string_literal(s):
            print(f"{i + 1}: String")
        elif is_character_literal(s):
            print(f"{i + 1}: Character")
        elif is_identifier(s):
            print(f"{i + 1}: Identifier")
        else:
            print(f"{i + 1}: INVALID!")

if __name__ == "__main__":
    main()
