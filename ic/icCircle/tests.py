from django.test import TestCase
from datetime import datetime
from icCircle.models import Post
from django.urls import reverse
from . import views
# Create your tests here.

class PostTests(TestCase):
    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    def test_show(self):
        response = self.client.get('posts/'+str(self.id))
        self.assertEqual(response.status_code, 404)