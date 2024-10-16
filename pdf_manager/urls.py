#add the urls for Fill_Futa

from django.urls import path
from . import views


urlpatterns = [
        path('Fill_Futa/<int:pk>/', views.Fill_Futa, name='Fill_Futa'),
        ]
