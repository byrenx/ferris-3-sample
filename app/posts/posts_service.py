# from protorpc import messages
# from ferris3 import auto_service, auto_method, Service
# import ferris3 as f3


# class PostsMessage(messages.Message):
#     title = messages.StringField(1)
#     content = messages.StringField(2)


# @f3.auto_service
# class PostsService(Service):

#     @f3.auto_method(returns=PostsMessage)
#     def get(self, request):
#         return PostsMessage(title="My First App With Ferris 3",content="Hello, Ferris!")

#     @f3.auto_method(returns=PostsMessage, name="list")
#     def list(self, request, title=(str,)):
#         return PostsMessage(title="My First App With Ferris 3",content="Hello, Ferris!")
from google.appengine.ext import ndb
from ferris3 import Model, Service, hvild, auto_service


class Post(Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()


@auto_service
class PostsService(Service):
    list = hvild.list(Post)
    get = hvild.get(Post)
    delete = hvild.delete(Post)
    insert = hvild.insert(Post)
    update = hvild.update(Post)
