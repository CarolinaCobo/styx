from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_explore, name='view_explore')

]
