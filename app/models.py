from django.db import models

# Create your models here.
class Movie(models.Model):
    name  = models.TextField(null=True,blank=True)
    file_id = models.CharField(max_length=500)
    def __str__(self):
        return self.name