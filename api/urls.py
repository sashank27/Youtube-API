from django.urls import path
from . import views

urlpatterns = [
    path('', views.VideoViewSet.as_view({'get': 'list'})),
]