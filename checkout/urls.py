from django.conf.urls import url
from .views import checkout
from .views import success

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^success/$', success, name='success')
]
