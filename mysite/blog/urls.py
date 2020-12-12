from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.PostList.as_view(), name='home'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path('',views.signin, name ='signin'),
    path('signout/',views.signout, name='signout'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]