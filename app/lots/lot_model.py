from google.appengine.ext import ndb
from ferris3 import Model

class Lot(Model):
    address = ndb.StringProperty()
    location = ndb.GeoPtProperty(required=True)
    sale_price = ndb.FloatProperty(default=0)
    #lots type: residential, commercial, industrial
    type = ndb.StringProperty(required=True)
    area = ndb.FloatProperty(default=0)
