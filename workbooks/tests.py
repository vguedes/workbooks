from django.test import TestCase

from inventory.models import Book 


class BookModelTest(TestCase):

    def test_string_representation(self):
        book = Book(title='Test Book')
        self.assertEqual(str(book), book.title)
