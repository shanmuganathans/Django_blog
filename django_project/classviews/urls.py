from django.urls import path
from . import views

urlpatterns = [
    path("template_view/", views.my_template_view, name = "my-template-view"),
    path("cbv_template_view/", views.MyTemplateView.as_view(), name="cbv-template-view"),
    path("form_view/", views.form_view_example, name ="form-view"),
    path("cbv_form_view/", views.MyFormView.as_view(), name ="cbv-form-view"),
    path("fbv_create_view/", views.fbv_create_view, name="fbv-create-view"),
    path("cbv_create_view/", views.CBVCreateView.as_view(), name="cbv-create-view"),
    path("fbv_list_view/", views.fbv_list_view, name="fbv-list-view"),
    path("cbv_list_view/", views.CBVListView.as_view(), name="cbv-list-view"),
    path("fbv_detail_view/<int:pk>", views.fbv_detail_view, name = "fbv-detail-view"),
    path("cbv_detail_view/<int:pk>", views.CBVDetailView.as_view(), name= "cbv-detail-view"),
    path("fbv_delete_view/<int:pk>", views.fbv_delete_view, name ="fbv-delete-view"),
    path("cbv_delete_view/<int:pk>", views.CBVDeleteView.as_view(), name ="cbv-delete-view"),
    path("fbv_update_view/<int:id>", views.fbv_update_view, name="fbv-update-view"),
    path("cbv_update_view/<int:id>", views.CBVUpdateView.as_view(), name="cbv-update-view"),
]
