from django.contrib import admin
from .models import Author,Publisher,BookCategory,Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','publish_date')


admin.site.register(Author)
admin.site.register(BookCategory)
admin.site.register(Publisher)
admin.site.register(Book,BookAdmin)
