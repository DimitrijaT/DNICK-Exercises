from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    embg = models.CharField(max_length=13)
    year_of_birth = models.IntegerField()
    country = models.CharField(max_length=50)
    biography = models.TextField(null=True, blank=True)


class Publication(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    house_number = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=17)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL)
    publication = models.ForeignKey(Author, on_delete=models.SET_NULL)


# Табелата во која што ќе ги имаме дефинирано моделот за публикација-автор
# Тука се чуваат парови автор-публикација
class PublicationAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL)
    publication = models.ForeignKey(Author, on_delete=models.SET_NULL)
