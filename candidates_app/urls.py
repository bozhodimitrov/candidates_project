from django.urls import path

from . import views


app_name = 'candidates_app'
urlpatterns = [
    path('', views.candidates, name='candidates'),
]
