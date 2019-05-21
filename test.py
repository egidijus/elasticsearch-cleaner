#!/bin/env python
from elasticsearch import Elasticsearch as es
from datetime import datetime, timedelta
import random, sys, uuid

es = es("http://localhost:9200")
# ilo = cu.IndexList(es)
"""
create some sample data, so we can use the cleaner to test the cleaning
"""

list_of_indexes = ["logstash-", "potato-"]
# list_of_indexes = ["logstash-", "application-", "potato-"]
days_of_indexes = -10
logs_per_index = 60
"""
-100 is starting from 100 days ago, until now
"""


def random_message(i=[0]):
    """
    returns a randomly generated message, useful for generating
    dynamic content.
    """
    nouns = ("puppy", "car", "rabbit", "potato", "monkey", "kitten", "giddy")
    verbs = ("runs", "hits", "jumps", "drives", "barfs", "poops", "sings")
    adv = ("crazily", "dutifully", "foolishly", "occasionally", "playfully",
           "bravely")
    adj = ("adorable", "clueless", "happy", "odd", "stupid", "cheeky", "lucky")
    num = random.randrange(0, 6)
    i[0] += 1
    print("count of calls to function ", i[0])
    dictionary = {}
    dictionary['count'] = str(i[0])
    dictionary['message'] = str(nouns[num] + ' ' + verbs[num] + ' ' +
                                adv[num] + ' ' + adj[num])
    return dictionary


def date_pad(date_string):
    """
    accept a day or month like 2 or 5,
    then pad it, prefix it with a "0" string.
    input: 2018.2.8
    ouput: 2018.02.08
    """
    if len(date_string) < 2:
        return "0" + date_string
    else:
        return date_string


def index_name(name_prefix="test-index-", when=timedelta()):
    """
    index name generator, with time range option.
    the idea is, you use this function to generate some index names
    for testing curator.
    """
    when_offset = datetime.now() + timedelta(days=when)
    when_date = [
        str(when_offset.year),
        date_pad(str(when_offset.month)),
        date_pad(str(when_offset.day))
    ]
    when_date = ".".join(when_date)
    index_name = name_prefix + when_date
    return index_name


# index_name(name_prefix="potato-index-", when=days_of_indexes)

# for day in range(days_of_indexes, 1, 1):
#     print("THE DAY IS:", day)


def create_indexes():
    try:
        for day in range(days_of_indexes, 1, 1):
            for item in list_of_indexes:
                for log in range(logs_per_index, 1, -1):
                    doc = {
                        'host':
                        '10.11.12.13' + str(log),
                        '@message':
                        random_message()['message'],
                        'log_level':
                        'INFO',
                        'count':
                        random_message()['count'],
                        '@timestamp':
                        datetime.now() + timedelta(
                            days=day, hours=random.randrange(1, 24))
                    }
                    # print(doc)
                    try:
                        response = es.index(
                            index=index_name(name_prefix=item, when=day),
                            op_type="create",
                            doc_type="log",
                            refresh="true",
                            id=uuid.uuid4(),
                            body=doc)
                        print(response)
                        # return response
                    except Exception as e:
                        print(
                            "Error on line {}".format(
                                sys.exc_info()[-1].tb_lineno),
                            type(e).__name__,
                            e,
                        )

            # es.indices.refresh(index=i)

    except Exception as e:
        print(
            "Error on line {}".format(sys.exc_info()[-1].tb_lineno),
            type(e).__name__,
            e,
        )


print(create_indexes())
