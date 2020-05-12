from django.urls import path
from qna import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]