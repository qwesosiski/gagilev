from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=20)
    surname = models.CharField("Фамилия",max_length=25)
    bitrhday = models.DateField("Биография", default='1999-06-02')
    bio = models.TextField("Описание")

    class Meta: 
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['surname','name']
        indexes = [
            models.Index(fields=['surname'])
        ]
        constraints = [
            models.UniqueConstraint (
                fields = ['surname','bio'],
                name = 'unique_surname_bio'
            ),
        ]

class Publisher(models.Model):
    name = models.CharField("Название",unique=True)

class Book(models.Model):
    title = models.CharField("Названиие",max_length=50)
    id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)