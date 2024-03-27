from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home, name='posts'),
    path("about/", views.about, name = "about"),
    path("post/create", views.create_post, name="create-post"),
    path("post/edit/<int:id>/",views.edit_post, name="edit-post"),
    path("post/delete/<int:id>/", views.delete_post , name="delete-post"),
    path("mail/",views.send_email_view, name="send-mail"),
    path("pagination/", views.test_pagination, name="pagination"),
    path("cbv_pagination/",views.PaginationTest.as_view(), name="cbv_pagination"),
    
]