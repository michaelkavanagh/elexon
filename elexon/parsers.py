from datetime import date, datetime


def expand_xml_item(elem, dict_: dict = {}, depth: int = 0):
    '''
    convert an XML node (and all of its children) into a nested
    list-dictionary-list-dictionary-... structure (mess)
    '''
    if len(elem) == 0:
        if elem.text is None:
            dict_[elem.tag] = None
        elif elem.tag == 'activeFlag':
            dict_[elem.tag] = True if elem.text == 'Y' else False
        else:
            dict_[elem.tag] = str_to_real_type(elem.text)

        return
    else:
        if depth == 0:
            # avoid unnecessary nesting under 'item' tags
            for child in elem:
                expand_xml_item(child, dict_, depth + 1)
        else:
            dict_2 = {}
            for child in elem:
                expand_xml_item(child, dict_2, depth + 1)

            if elem.tag in dict_.keys():
                # Deal with multiple child nodes with the same name:
                # form a nested list within the dict value (see B1610)
                try:
                    dict_[elem.tag].append(dict_2)
                except:
                    temp = dict_[elem.tag]
                    dict_[elem.tag] = []
                    dict_[elem.tag].append(temp)
                    dict_[elem.tag].append(dict_2)
            else:
                dict_[elem.tag] = dict_2


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
        return datetime.strptime(s, '%d/%m/%Y %H:%M:%S')
    except ValueError:
        pass
    try:
        return datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        pass
    try:
        return datetime.strptime(s, '%d/%m/%Y')
    except ValueError:
        pass
    try:
        return datetime.strptime(s, '%Y-%m-%d')
    except ValueError:
        pass
    return s
