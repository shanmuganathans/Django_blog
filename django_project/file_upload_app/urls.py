from django.urls import path
from . import views
urlpatterns = [
    path('upload/', views.uploda_file, name="upload_file"),
    path("success/", views.upload_success, name = "upload_success"),
]
