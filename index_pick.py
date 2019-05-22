#!/bin/env python
from datetime import datetime, timedelta
import sys, uuid


def date_pad(date_string):
    """
    accept a day or month like 2 or 5,
    then pad it, prefix it with a "0" string.
    input: 2018.2.8
    ouput: 2018.02.08
    """
    try:
        if len(date_string) < 2:
            return "0" + date_string
        else:
            return date_string
    except Exception as e:
        print(
            "Error on line {}".format(sys.exc_info()[-1].tb_lineno),
            type(e).__name__,
            e,
        )


def index_name(name_prefix="test-index-", when=timedelta()):
    """
    index name generator, with time range option.
    the idea is, you use this function to generate valid elasticsearch names.
    this would be used for creating indexes and data for testing,
    and for slecting which index you want to delete.
    """
    try:
        when_offset = datetime.now() + timedelta(days=when)
        when_date = [
            str(when_offset.year),
            date_pad(str(when_offset.month)),
            date_pad(str(when_offset.day))
        ]
        when_date = ".".join(when_date)
        index_name = name_prefix + when_date
        return index_name
    except Exception as e:
        print(
            "Error on line {}".format(sys.exc_info()[-1].tb_lineno),
            type(e).__name__,
            e,
        )
