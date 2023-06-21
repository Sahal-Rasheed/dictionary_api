from django.db import models

# Create your models here.

class Dictionary(models.Model):
    label        = models.CharField(max_length=100)
    description  = models.TextField()
    search_count = models.IntegerField(default=0)

    def increment_search_count(self):
        self.search_count += 1
        self.save()