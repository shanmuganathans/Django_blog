from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm
from .models import Contact

from django.http import HttpResponse

# Create your views here.

def my_template_view(request):
    context = { "title": " My django class"}
    return render(request, "classviews/my_template.html", context)


class MyTemplateView(TemplateView):
    template_name = "classviews/my_template.html"
    
    def get_context_data(self):
        context = { "title": " My django class based views"}
        return context  
        
def form_view_example(request):
    if request.method == "GET":
        form = ContactForm()
        context = {"form":form}
        return render(request, "classviews/form_template.html",context)




class MyFormView(FormView):
    template_name = "classviews/form_template.html"
    form_class = ContactForm
    
    def form_valid(self, form):
        # data = form.cleaned_data
        # print(data)
        form.save()
        return redirect("cbv-form-view")