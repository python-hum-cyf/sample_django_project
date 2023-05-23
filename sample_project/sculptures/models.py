from django.db import models

# Create your models here.
class Sculpture(models.Model):
    title = models.CharField(blank=False, max_length=150, default='Unknown')
    author = models.ForeignKey('authors.Author', on_delete=models.DO_NOTHING, related_name='sculptures',
                               to_field='name', default='Unknown')

    def __str__(self):
        return f'{self.id}: {self.title}'
