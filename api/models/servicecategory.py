from google.appengine.ext import ndb

class ServiceCategoryModel(ndb.Model):
    idcategory = ndb.StringProperty()
    category = ndb.StringProperty()
    # title = db.StringProperty()
    # body = db.TextProperty()
    # created = db.DateTimeProperty(auto_now_add=True)
    
#
