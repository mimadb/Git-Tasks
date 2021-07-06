from django.db import models

class BlogPost(models.Model):
    name = models.CharField(max_length = 50)
    thetext = models.CharField(max_length = 300)
    def __str__(self):
        return self.name
