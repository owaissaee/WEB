from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='account_signup'),
    path('profile/', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    path('settings/', login_required(TemplateView.as_view(template_name='registration/account_settings.html')), name='account_settings'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]