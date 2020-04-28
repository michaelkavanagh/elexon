from datetime import date, datetime

def str_to_real_type(s):
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    try:
        return datetime.strptime(s, '%d/%m/%y %H:%M:%S')
    except ValueError:
        pass
    try:
        return datetime.strptime(s, '%d/%m/%y')
    except ValueError:
        pass
    return s
