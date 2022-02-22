from django.contrib import admin
from django.urls import path
from problems import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('created',views.createddd)
]
