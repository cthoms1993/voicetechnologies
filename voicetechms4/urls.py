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
from checkout import urls as urls_checkout
from django.conf import settings
from django.conf.urls.static import static
from staff.views import all_staff
from blog import urls as urls_blog
from contact import urls as urls_contact

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', all_products, name='index'),
                  url(r'^index/', index, name="index"),
                  url(r'^accounts/', include(urls_accounts)),
                  url(r'^products/', include(urls_products)),
                  url(r'^cart/', include(urls_cart)),
                  url(r'^search/', include(urls_search)),
                  url(r'^checkout/', include(urls_checkout)),
                  url(r'^about/', all_staff, name='about'),
                  url(r'^blog/', include(urls_blog)),
                  url(r'^contact/', include(urls_contact)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
