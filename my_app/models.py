from django.db import models

# Create your models here.
class Search(models.Model):

    def __str__(self) :
        return '{}'.format(self.search)
        #return self.search

    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)