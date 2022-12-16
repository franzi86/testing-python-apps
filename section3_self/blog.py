from section3_self.post import Post


class Blog(object):
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self) -> str:
        return "{} by {} ({} posts)".format(self.title, self.author, len(self.posts))

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts],
        }
