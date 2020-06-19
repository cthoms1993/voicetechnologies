from django.conf.urls import url, include
from .views import dictation_products, software_products, speech_products

urlpatterns = [
    url(r'^$', dictation_products, name='dictation_products'),
    url(r'^speech/', speech_products, name='speech_products'),
    url(r'^software/', software_products, name='software_products'),
]
