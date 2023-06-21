from django.db import models

# Create your models here.

class Dictionary(models.Model):
    label        = models.CharField(max_length=100)
    description  = models.TextField()
    search_count = models.IntegerField(default=0)

    # Sets verbose names for the admin interface
    class Meta:
        verbose_name = 'dictionary'
        verbose_name_plural = 'dictionaries'

    # Method to increment value of search_count
    def increment_search_count(self):
        self.search_count += 1
        self.save()