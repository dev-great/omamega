from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('account_type/', views.account_type, name='account_type'),
    path('my_properties/', views.my_properties, name='my_properties'),
    path('maintainance/', views.maintainance, name='maintainance'),
    path('tenant/', views.tenant, name='tenant'),
    path('personal_info/', views.personal_info, name='personal_info'),
    path('invoice/', views.invoice, name='invoice'),
]
