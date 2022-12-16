from unittest import TestCase

from section3_self.post import Post


class TestPost(TestCase):
    def test_create_post(self):
        p = Post("Test", "Test Content")

        self.assertEqual("Test", p.title)
        self.assertEqual("Test Content", p.content)

    def test_json(self):
        p = Post("Test", "Test Content")
        expect = {"title": "Test", "content": "Test Content"}

        self.assertDictEqual(expect, p.json())
