from django.db import models
from MaintenanceRequest.choices import STATUS_CHOICES
from Tenant.models import Tenant
from Property.models import Property


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_on']


class MaintenanceRequest(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    issue_description = models.TextField()
    date_reported = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    assigned_vendor = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, null=True)
    date_completed = models.DateTimeField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.tenant)

    class Meta:
        ordering = ['-updated_on']
