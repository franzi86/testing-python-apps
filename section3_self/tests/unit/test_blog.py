from unittest import TestCase

from section3_self.blog import Blog as blog


class TestBlog(TestCase):
    def test_create_blog(self):
        b = blog("Test", "Anton Blume")

        self.assertEqual("Test", b.title)
        self.assertEqual("Anton Blume", b.author)
        self.assertListEqual(list(), b.posts)

    def test_repr(self):
        b = blog("Test", "Anton Blume")
        b2 = blog("My Day", "Rolf")

        self.assertEqual(b.__repr__(), "Test by Anton Blume (0 posts)")
        self.assertEqual(b2.__repr__(), "My Day by Rolf (0 posts)")

    def test_repr_multible(self):
        b = blog("Test", "Anton Blume")
        b.posts = ["Test"]
        b2 = blog("My Day", "Rolf")
        b2.posts = ["Test", "another"]

        self.assertEqual(b.__repr__(), "Test by Anton Blume (1 posts)")
        self.assertEqual(b2.__repr__(), "My Day by Rolf (2 posts)")

    def test_json(self):
        b = blog("Test", "Anton Blume")
        expect = {
            "title": "Test",
            "author": "Anton Blume",
            "posts": [],
        }

        self.assertDictEqual(expect, b.json())
