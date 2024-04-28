from django.urls import path 
from . import views
urlpatterns = [
    path('students' , views.transfer_data),
    path('index2.html' , views.index2_view)
]