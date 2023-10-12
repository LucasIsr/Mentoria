
from django.urls import path, include

urlpatterns = [
    path('resendsrefac/',include('app_resendsrefac.urls'),name='resendsrefac'),
]
