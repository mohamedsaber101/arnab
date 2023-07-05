from django.db import models

# Create your models here.
class Arnaba(models.Model):
    STATE_CHOICES = (
        ('فاضية', 'فاضية'),
        ('مليانة', 'مليانة'),
        ('متلقحة', 'متلقحة'),
        ('مرضعة', 'مرضعة'),
        ('حامل و مرضعة', 'حامل و مرضعة'),
        ('متلقحة و مرضعة', 'متلقحة و مرضعة'),
    )
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    birth_date = models.DateField(default=None)
    birth_times = models.IntegerField(default=None)
    talqeeh_times = models.IntegerField(default=None)
    state = models.CharField(max_length=200, choices= STATE_CHOICES, default='emmm')
    image =  models.CharField(max_length=200, default='arnaba.png')

    


class Arnab(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    age = models.IntegerField()
    


