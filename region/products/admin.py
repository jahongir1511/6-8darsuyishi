from django.contrib import admin
from .models import Review, Books, Author, CategoryBooks, BookAuthor
# Register your models here.

admin.site.register(Author)
admin.site.register(CategoryBooks)
admin.site.register(Books)
admin.site.register(BookAuthor)
admin.site.register(Review)



