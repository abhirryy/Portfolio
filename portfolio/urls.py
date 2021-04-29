"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from mysite import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name = 'home'),
    # path('contact/', views.contact, name = 'contact')
]
# this help us to use the static file.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# django make using a static file easy and is used as a collective data and with
# just a command we can collect all static file and keep it inside the project static folder i.e python manage.py collectstatic
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
