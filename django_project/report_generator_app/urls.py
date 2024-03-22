from django.urls import path
from . import views

urlpatterns = [
    path("view/",views.ReportListView.as_view(), name ="report_list_view"),
    path("generate_csv", views.generate_csv, name ="generate_csv"),
    path("generate_pdf", views.generate_pdf, name = "generate_pdf"),
]
