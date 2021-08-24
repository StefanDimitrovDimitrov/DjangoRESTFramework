from django.contrib import admin

# Register your models here.
from books_api.models import BookModel

admin.site.register(BookModel)