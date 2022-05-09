from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<slug:slug>', views.occupied, name='occupied'),
    path('free/<slug:slug>', views.free, name='free')
]
