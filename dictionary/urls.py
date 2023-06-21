from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from api.views import DictionaryView

# Define the router for the api using viewset
router = DefaultRouter()
router.register('dictionary', DictionaryView, basename='dict')

urlpatterns = [
    path('admin/', admin.site.urls),  
] + router.urls
