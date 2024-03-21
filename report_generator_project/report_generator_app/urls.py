from django.urls import path
from . import views

urlpatterns = [
    path('generate-csv/', views.generate_csv, name='generate_csv'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('', views.ReportListView.as_view(), name='report_list_view'),
]
