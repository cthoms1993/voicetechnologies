"""voicetechms4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include
from accounts import urls as urls_accounts
from home.views import index
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from products.views import all_products
from .settings import MEDIA_ROOT
from django.conf import settings
from django.views import static
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', all_products, name='index'),
                  url(r'^index/', index, name="index"),
                  url(r'^accounts/', include(urls_accounts)),
                  url(r'^products/', include(urls_products)),
                  url(r'^cart/', include(urls_cart)),
                  url(r'^search/', include(urls_search)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
