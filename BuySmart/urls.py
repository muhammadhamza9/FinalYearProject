"""BuySmart URL Configuration

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
from apps.core.views import home, contact
from apps.products.views import product_detail, cat_detail
from apps.cart.views import cart_detail
from apps.products.apis import cart_api


urlpatterns = [
    path('', home, name="home"),
    path('cart/', cart_detail, name="cart"),
    path('contact/', contact, name="contact"),
    path('admin/', admin.site.urls),

    # API
    path('api/add_to_cart/', cart_api, name='cart_api'),

    path('<slug:category_slug>/<slug:slug>/', product_detail, name="product_detail"),
    path('<slug:slug>/', cat_detail, name="cat_detail"),

]
