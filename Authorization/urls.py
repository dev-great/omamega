from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'Authorization'

urlpatterns = [
    path('login/', custom_login_view, name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('core:index')), name='logout'),
    path('changePassword/', changePassword, name='changePassword'),
]
