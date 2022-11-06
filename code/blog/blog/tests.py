from django.test import TestCase

from .models import Post

# Create your tests here.

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="this is a tests!")