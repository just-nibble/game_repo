from django.db import models

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=20)
    genre = models.CharField(max_length=10)
    platform = models.CharField(max_length=10)

    def __str__(self):
        return('{}'.format(self.title))
