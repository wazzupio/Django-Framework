from django.contrib import admin
from django.urls import path
from mainapp.views import products

app_name = 'mainapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products, name='products'),
]
