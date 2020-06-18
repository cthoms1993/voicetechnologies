from django.conf.urls import url, include
from .views import all_staff

urlpatterns = [
    url(r'^$', all_staff, name='staff'),
    ]