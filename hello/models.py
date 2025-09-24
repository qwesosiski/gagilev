from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=20)
    surname = models.CharField("Фамилия",max_length=25)
    bitrhday = models.DateField("Биография")
    bio = models.TextField("Описание")

class Publisher(models.Model):
    name = models.CharField("Название",unique=True)

class Book(models.Model):
    title = models.CharField("Названиие",max_length=50)
    id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)