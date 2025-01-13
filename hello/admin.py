from django.contrib import admin
from .models import Book, Genre, Suggestor, Author

# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Suggestor)
admin.site.register(Author)