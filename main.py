#!/bin/env python
from elasticsearch import Elasticsearch as es
import sys
import index_pick as ipick
import json

ess = es("http://localhost:9200")

older_than_days_delete = 9
list_of_indexes = ["logstash-", "potato-"]


def prettyfy_json(json_object):
    try:
        return json.dumps(json_object, indent=4, sort_keys=True)
    except Exception as e:
        print(
            "Error on line {}".format(sys.exc_info()[-1].tb_lineno),
            type(e).__name__,
            e,
        )


esattrs = vars(es)

print(', '.join("%s: %s" % item for item in esattrs.items()))

# nice_indexes = es.CatClient.indices(index="*")

print("hello giddy", ess.CatClient())

# print(ipick.index_name("tomato-", range(older_than_days_delete, )))

# # filebeat-ovpn-2019.04.09
# def list_indexes_for_deletion(older_than_days_delete=older_than_days_delete,
#                               prefix='log*'):
#     regex_index_list = ilo.filter_by_regex(kind='prefix', value=prefix)
#     print(regex_index_list)
#     ilo.filter_by_age(
#         source='name',
#         direction='older',
#         timestring='%Y.%m.%d',
#         unit='days',
#         unit_count=older_than_days_delete)

# list_indexes_for_deletion()
