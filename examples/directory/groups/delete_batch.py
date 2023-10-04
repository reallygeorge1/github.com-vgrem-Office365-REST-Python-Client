"""
Delete groups in batch mode

https://learn.microsoft.com/en-us/graph/api/group-delete?view=graph-rest-1.0&tabs=http
"""

from office365.graph_client import GraphClient
from tests.graph_case import acquire_token_by_username_password

client = GraphClient(acquire_token_by_username_password)

result = client.groups.get_all().execute_query()
print("Total groups count (before): {0}".format(len(result)))

groups = client.groups.get().top(4).execute_query()
for cur_grp in groups:
    cur_grp.delete_object()
client.execute_batch()
print("Groups have been deleted")

result = client.groups.get_all().execute_query()
print("Total groups count (after): {0}".format(len(result)))
