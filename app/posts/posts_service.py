import ferris3 as f3
from app.posts.post_model import Post

PostMessage = f3.model_message(Post)
PostListMessage = f3.list_message(PostMessage)

@f3.auto_service
class PostsService(f3.Service):
    list = f3.hvild.list(Post)
    paginated_list = f3.hvild.paginated_list(Post)
    get = f3.hvild.get(Post)
    delete = f3.hvild.delete(Post)
    insert = f3.hvild.insert(Post)
    update = f3.hvild.update(Post)

    @f3.auto_method(returns=PostListMessage, name="all")
    def list_all(self, request):
        '''
        return list of all posts as a PostMessage
        '''
        posts = Post.query()
        if not posts:
            raise f3.NotFoundException()
        list_message = f3.messages.serialize_list(PostListMessage, posts)
        return list_message


    @f3.auto_method(returns=PostMessage, name="get_by_title")
    def get_by_title(self, request, title=(str,)):
        query = Post.query(Post.title==title)
        post = query.get()
        if not post:
            raise f3.NotFoundException()
        if not post.key.kind() == 'Post':
            raise f3.InvalidRequestException()
        message = f3.messages.serialize(PostMessage, post)
        return message
