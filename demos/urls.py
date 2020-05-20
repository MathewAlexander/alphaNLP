from django.urls import path
from . import views

urlpatterns = [
    path("", views.demo_index, name="demo_index"),
    path("qa", views.qa_inference, name="qa_inference"),
]