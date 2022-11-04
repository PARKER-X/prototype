from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', views.login_page, name='Login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name='Logout'),
    path('accounts/register/', views.register_page, name='Register'),
]
