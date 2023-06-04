from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_api.as_view(), name='api'),
]