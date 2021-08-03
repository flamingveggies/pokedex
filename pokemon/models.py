from django.db import models

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.URLField()
    image_back = models.URLField()

    def __str__(self):
        return self.name

class Type(models.Model):
    type = models.CharField(max_length=50)
    pokemon = models.ManyToManyField(Pokemon, related_name='types')

    def __str__(self):
        return self.type
    
