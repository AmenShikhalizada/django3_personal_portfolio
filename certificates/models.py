from django.db import models

class Certificate(models.Model):
    title  = models.CharField(max_length=100)
    description  = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    document = models.FileField(upload_to='portfolio/images/', null=True)

    def __str__(self):
        return self.title