from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.hello_view, name='start_hello'),
    path('', views.hello_view, name='start_hello'),
]