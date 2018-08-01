from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test", "Test Author")
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
        self.assertEqual(len([]), len(b.posts))

    def test_repr(self):
        b = Blog("Test", "Test Author")
        b2 = Blog("My Day", "John")
        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by John (0 posts)')

    def test_repr_multiple_post(self):
        b = Blog("Test", "Test Author")
        b.posts = ['test']
        b2 = Blog("My Day", "John")
        b2.posts = ['test', 'test2']
        self.assertEqual(b.__repr__(), 'Test by Test Author ({} post{})'.format(
            len(b.posts), 's' if len(b.posts) != 1 else ''
        ))
        self.assertEqual(b2.__repr__(), 'My Day by John ({} post{})'.format(
            len(b2.posts), 's' if len(b2.posts) != 1 else ''
        ))


