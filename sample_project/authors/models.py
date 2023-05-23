from django.db import models

# Create your models here.

class Author(models.Model):
    class AuthorCountry(models.TextChoices):
        UNKNOWN = 'Unknown'
        FRANCE = 'France'
        ITALY = 'Italy'
        GERMANY = 'Germany'
        NETHERLANDS = 'Netherlands'
    name = models.CharField(blank=False, default='Unknown',
                            max_length=150, unique=True)
    year_of_birth = models.IntegerField(blank=True, null=True)
    year_of_death = models.IntegerField(blank=True, null=True)
    country_of_origin = models.CharField(blank=False,
                                         default=AuthorCountry.UNKNOWN,
                                         max_length=25,
                                         choices=AuthorCountry.choices)

    def __str__(self):
        return f'{self.id}: {self.name}'

