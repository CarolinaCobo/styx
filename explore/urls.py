from django.urls import path
from . import explore


urlpatterns = [
    path('', explore.view_explore, name='view_explore'),

]
