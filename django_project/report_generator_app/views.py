from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.views.generic.list import ListView
from .models import ReportData
import csv

from xhtml2pdf import pisa
from django.template.loader import get_template

class ReportListView(ListView):
    template_name = "report_generator_app/report_list_template.html"
    context_object_name = "data"
    queryset = ReportData.objects.all()
    

def generate_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Dispositon"] = 'attachment'; filename="report.csv"
    
    writer = csv.writer(response)
    writer.writerow(['Name','Age','Email'])
    
    queryset = ReportData.objects.all()
    for item in queryset:
        writer.writerow([item.name, item.age, item.email])
    
    return response

def generate_pdf(request):
    template_path = "report_generator_app/pdf_template.html"
    queryset = ReportData.objects.all()
    context = {"data": queryset}
    
    response = HttpResponse(content_type= "application/pdf")
    response["Content-Disposition"] = "attachement"; filename = "report.pdf"
    
    template = get_template(template_path)
    html = template.render(context)
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("PDF generation failed")
    
    return response
    
    