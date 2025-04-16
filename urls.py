"""
URL configuration for mydjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('signin/', views.signin),
    path('devices/', views.devices),    
    path('cart/', views.cart),
    path('Laptops/', views.laptops),
    path('mobiles/', views.mobiles),
    path('screens/', views.screens),
    path('tablets/', views.tablets),
    path('/', views.redirect_to_home),  
    # path('/some-url/',some_view),  # Example of a URL pattern with a view function

    # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/', views.cart, name='cart'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)