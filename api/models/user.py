# modul api.models.user
from google.appengine.ext import ndb

class UserModel(ndb.Model):
    username = ndb.StringProperty(indexed=True)
    realname = ndb.StringProperty(indexed=True)
    password = ndb.StringProperty(indexed=False)
    # group = ndb.StringProperty(indexed=False)     # GROUP { MGR, CUS, TEC }
    group = ndb.StringProperty(choices=('MNGR', 'CUST', 'TECH'), indexed=True)