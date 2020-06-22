from django.conf.urls import url, include
from .views import all_products, win_voice_pro, win_voice_web, form_stream

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^winvoicepro/$', win_voice_pro, name='winvoicepro'),
    url(r'^winvoiceweb/$', win_voice_web, name='winvoiceweb'),
    url(r'^formstream/$', form_stream, name='formstream'),

]
