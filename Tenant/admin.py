from django.contrib import admin

from Tenant.models import LeaseAgreement, Payment, Tenant

# Register your models here.
admin.site.register(LeaseAgreement)
admin.site.register(Tenant)
admin.site.register(Payment)
