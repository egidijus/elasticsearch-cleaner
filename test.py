#!/bin/env python
from elasticsearch import Elasticsearch as es
from datetime import datetime, timedelta
import random, sys, uuid
import index_pick as ipick

es = es("http://localhost:9200")
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
    try:

        nouns = ("puppy", "car", "rabbit", "potato", "monkey", "kitten",
                 "giddy")
        verbs = ("runs", "hits", "jumps", "drives", "barfs", "poops", "sings")
        adv = ("crazily", "dutifully", "foolishly", "occasionally",
               "playfully", "bravely")
        adj = ("adorable", "clueless", "happy", "odd", "stupid", "cheeky",
               "lucky")
        num = random.randrange(0, 6)
        i[0] += 1
        print("count of calls to function ", i[0])
        dictionary = {}
        dictionary['count'] = str(i[0])
        dictionary['message'] = str(nouns[num] + ' ' + verbs[num] + ' ' +
                                    adv[num] + ' ' + adj[num])
        return dictionary
    except Exception as e:
        print(
            "Error on line {}".format(sys.exc_info()[-1].tb_lineno),
            type(e).__name__,
            e,
        )


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
                            index=ipick.index_name(name_prefix=item, when=day),
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
