"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.views import *
from shop.settings import MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', str1 , name='str1'),
    path('detail/<int:id>',detail,name = 'detail'),
    path('favorites/<int:id>',favorites,name = 'favorites'),
    path('favorite',favorites_page,name = 'favorite'),
    path('cards/',cards,name = 'cards'),
    path('addcart/<int:id>',addcart,name = 'addcart'),
    path('aith/', auth, name='auth'),

]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
