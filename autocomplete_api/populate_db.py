
from autocomplete_api.db import ac
from steem import Steem


def init_db():
    print("Fetching all usernames")
    all_usernames = Steem().get_all_usernames()
    print("Fetched. Total: %s" % all_usernames)
    for username in all_usernames:
        ac.store(username)
