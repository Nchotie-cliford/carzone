
from django.urls import path
from .views import home
from .views import about
from .views import services
from .views import contact


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('Services', services, name='services'),
    path('Contact', contact, name='contact'),
]
