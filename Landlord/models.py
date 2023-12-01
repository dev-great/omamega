from django.db import models
from Chat.models import Communication
from Property.models import Property
# Create your models here.


class PropertyPortfolio(models.Model):
    properties = models.ManyToManyField(Property)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.properties)

    class Meta:
        ordering = ['-updated_on']


class ClientLandlord(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=255)
    property_portfolio = models.ForeignKey(
        PropertyPortfolio, on_delete=models.CASCADE)
    real_time_counter = models.BooleanField()
    communications = models.ManyToManyField(Communication)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_on']
