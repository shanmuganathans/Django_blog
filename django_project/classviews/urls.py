from django.urls import path
from . import views

urlpatterns = [
    path("template_view/", views.my_template_view, name = "my-template-view"),
    path("cbv_template_view/", views.MyTemplateView.as_view(), name="cbv-template-view"),
    path("form_view/", views.form_view_example, name ="form-view"),
    path("cbv_form_view/", views.MyFormView.as_view(), name ="cbv-form-view"),
]
