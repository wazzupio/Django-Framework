from django.contrib import admin
from django.urls import path
from authapp.views import login, register, logout, profile

app_name = 'authapp'

urlpatterns = [
    path('profile/admin/', admin.site.urls),
    path('', login, name='login'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
