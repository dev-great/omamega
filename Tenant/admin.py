from django.contrib import admin

from Tenant.models import LeaseAgreement, Payment, PaymentHistory, Tenant

# Register your models here.
admin.site.register(LeaseAgreement)
admin.site.register(Tenant)
admin.site.register(PaymentHistory)
admin.site.register(Payment)
