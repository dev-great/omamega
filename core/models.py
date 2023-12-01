from django.db import models

# Create your models here.


class Testimonial(models.Model):
    author = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.author


class TrustedBrand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brand_logos/')

    def __str__(self):
        return self.name
