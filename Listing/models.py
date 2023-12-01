from django.db import models
from Property.models import Property


class PropertyListing(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    rental_price = models.DecimalField(
        max_digits=50, decimal_places=2, null=True, blank=True)
    selling_price = models.DecimalField(
        max_digits=50, decimal_places=2, null=True, blank=True)
    asking_price = models.DecimalField(
        max_digits=50, decimal_places=2, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.property)

    class Meta:
        ordering = ['-updated_on']
