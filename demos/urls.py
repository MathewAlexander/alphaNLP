from django.urls import path
from . import views

urlpatterns = [
    path("", views.demo_index, name="demo_index"),
    path("<int:pk>/", views.demo_detail, name="demo_detail"),
    path("qa", views.demo_qa, name="demo_qa"),
]