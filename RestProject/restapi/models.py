from django.db import models

# Create your models here.

class Occurrence(models.Model):

    STATES_CHOICES = [('por validar','por validar'), ('validado','validado'), ('resolvido','resolvido')]
    CATEGORIES_CHOICES = [('CONSTRUCTION', 'CONSTRUCTION'),
                          ('SPECIAL_EVENT', 'SPECIAL_EVENT'),
                          ('INCIDENT', 'INCIDENT'),
                          ('WEATHER_CONDITION', 'WEATHER_CONDITION'),
                          ('ROAD_CONDITION', 'ROAD_CONDITION')]

    description = models.CharField(max_length=100)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    owner = models.ForeignKey('auth.User', related_name='occurences', on_delete=models.CASCADE)
    initial_date = models.DateTimeField(auto_now_add=True) # É adicionada na criação
    edit_date = models.DateTimeField(blank=True, null=True) # É adiciona quando é feita uma edicao
    state = models.CharField(choices=STATES_CHOICES, default='por validar', max_length=100)
    category = models.CharField(choices=CATEGORIES_CHOICES, max_length=100)

    def __str__(self):
        return self.description
