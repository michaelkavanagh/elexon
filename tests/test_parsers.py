import datetime

import pytest

from elexon import parsers


def test_str_to_real_type():
    assert parsers.str_to_real_type('test string') == 'test string'
    assert parsers.str_to_real_type('3') == 3
    assert parsers.str_to_real_type('3.14') == 3.14
    assert parsers.str_to_real_type('2020-06-03 10:11:12') == \
        datetime.datetime(2020, 6, 3, 10, 11, 12)
    assert parsers.str_to_real_type('2020-06-03') == \
        datetime.date(2020, 6, 3)
    # assert parsers.str_to_real_type('10:11:12 +00') == '10:11:12'
    # assert parsers.str_to_real_type('10:11:12 +00') == \
    #     datetime.time(10, 11, 12)
