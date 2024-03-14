from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home, name='posts'),
    path("about/", views.about, name = "about"),
    path("post/create", views.create_post, name="create-post"),
    path("post/edit/<int:id>/",views.edit_post, name="edit-post"),
    path("post/delete/<int:id>/", views.delete_post , name="delete-post"),
    
]