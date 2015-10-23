from google.appengine.ext import ndb
from ferris3 import Model

class Post(Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
