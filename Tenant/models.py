from django.db import models
from django.conf import settings
from Tenant.choices import PAYMENT_METHOD_CHOICES
from Chat.models import Communication

# Create your models here.


class LeaseAgreement(models.Model):
    note = models.TextField()
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note

    class Meta:
        ordering = ['-updated_on']


class Tenant(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=255)
    lease_agreement = models.OneToOneField(
        LeaseAgreement, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_on']


class Payment(models.Model):
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return self.payment_method

    class Meta:
        ordering = ['-payment_date']
