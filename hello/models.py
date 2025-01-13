from django.db import models
import datetime
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Genres"
    
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    
class Suggestor(models.Model):
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name}'
    

class Book(models.Model):
    name = models.CharField(max_length=50)
    synopsis = models.CharField(max_length=1000, null = True, blank = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/product/')
    amazon_link = models.URLField(max_length=200, null = True, blank = True)
    suggestor = models.ForeignKey(Suggestor, on_delete=models.CASCADE, default = 1)
    date = models.DateField(default = datetime.datetime.today)
    bn_link = models.URLField(max_length=200, null = True, blank = True)


    def __str__(self):
        return self.name


