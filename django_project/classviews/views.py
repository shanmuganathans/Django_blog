from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact
from django.contrib import messages
from django.http import HttpResponse


from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView, DeleteView
from django.views.generic.detail import DetailView


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
    
def fbv_create_view(request):
    if request.method == "GET":
        context = {'form': ContactForm()}
        return render(request,"classviews/form_template.html",context)
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"The contact is created syccessfully..!")
            context = {'form': ContactForm()}
            return render(request, "classviews/form_template.html", context)
        else:
            context= {
                "form": form
            }
            messages.error(request,"Please correct the errors")
            return render(request, "classviews/form_template.html", context)


class CBVCreateView(CreateView):
    form_class = ContactForm
    template_name = "classviews/form_template.html"
    
    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(f"contact save:{instance}")


def fbv_list_view(request):
    contacts = Contact.objects.all()
    context = {
        'contacts':contacts
    }
    return render(request,"classviews/list_template.html", context)


class CBVListView(ListView):
    template_name = "classviews/list_template.html"
    context_object_name = "contacts"
    queryset = Contact.objects.all()

def fbv_detail_view(request, pk):
    try:
        obj = Contact.objects.get(id=pk)
    except Contact.DoesNotExist:
        raise Http404
    context = {"object": obj }
    return render(request,"classviews/detail_template.html", context)

class CBVDetailView(DetailView):
    template_name = "classviews/detail_template.html"
    pk_url_kwarg = 'pk'
    queryset = Contact.objects.all()
    
    
def fbv_delete_view(request, pk):
    obj = get_object_or_404(Contact, id=pk)
    if request.method == "GET":
        context = {"object": obj}
        return render(request,"classviews/delete_template.html",context)
    if request.method == "POST":
        obj.delete()
        return HttpResponse("Deleted successfully..!")
    

class CBVDeleteView(DeleteView):
    template_name = "classviews/delete_template.html"
    pk_url_kwarg = 'pk'
    queryset = Contact.objects.all()
    
    def form_valid(self, form):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse("Deleted successfully..!")