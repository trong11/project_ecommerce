from django.db import models

# Create your models here.
class Author(models.Model):
    author_name  = models.CharField(max_length=200, unique=True)
    author_dob = models.DateField()
    author_phonenumber = models.CharField(max_length=200, unique=True)
    author_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.author_name

class BookCategory(models.Model):
    cate_name  = models.CharField(max_length=200, unique=True)
    cate_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.cate_name

class Publisher(models.Model):
    pub_name  = models.CharField(max_length=200, unique=True)
    pub_phonenumber = models.CharField(max_length=200, unique=True)
    pub_address = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.pub_name


class Book(models.Model):
    book_name  = models.CharField(max_length=200, unique=True)
    import_price = models.IntegerField()
    book_description = models.TextField(max_length=500, blank=True)
    publish_date = models.DateField()
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    bookcategory = models.ForeignKey(BookCategory,on_delete = models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete = models.CASCADE)

    def __str__(self):
        return self.book_name
