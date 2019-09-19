from django.db import models
from .library import Library
from .librarian import Librarian

class Book(models.Model):
    # Title (CharField)
    # ISBN number (CharField)
    # Author (CharField)
    # Year published (IntegerField)
    title = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField()
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, default=None, null=True, on_delete=models.CASCADE)

