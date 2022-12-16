from unittest import TestCase

from section3_self.blog import Blog as blog


class TestBlog(TestCase):
    def test_create_post(self):
        b = blog("Test", "Anton Blume")
        b.create_post("Post", "Post Content")

        self.assertEqual(1, len(b.posts))

    def test_json(self):
        b = blog("Test", "Anton Blume")
        b.create_post("Post", "Post Content")
        expect = {
            "title": "Test",
            "author": "Anton Blume",
            "posts": [{"title": "Post", "content": "Post Content"}],
        }

        self.assertDictEqual(expect, b.json())
