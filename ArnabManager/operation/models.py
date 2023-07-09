from django.db import models

# Create your models here.
class Arnaba(models.Model):
    STATE_CHOICES = (
        ('fadya', 'fadya'),
        ('malyana', 'malyana'),
        ('Metlaqa7a', 'Metlaqa7a'),
        ('Morde3a', 'Morde3a'),
        ('7amel w Morde3a', '7amel w Morde3a'),
        ('Metlaqa7a w Morde3a', 'Metlaqa7a w Morde3a'),
    )
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200,unique=True)
    desc = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    age = models.IntegerField()
    birth_times = models.IntegerField(default=None)
    talqeeh_times = models.IntegerField(default=None)
    state = models.CharField(max_length=200, choices= STATE_CHOICES, default='fadya')
    talqeeh_zakar =  models.ForeignKey("Arnab", on_delete=models.SET_NULL, blank=True, null=True)
    image =  models.CharField(max_length=200, default='arnaba.png')

    


class Arnab(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200,unique=True)
    desc = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    age = models.IntegerField()
    image =  models.CharField(max_length=200, default='arnab.png')

    


