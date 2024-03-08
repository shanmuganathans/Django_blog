from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Contact
from .forms import PostForm

from django.contrib import messages


def home(request):
    
    all_data = Post.objects.all()
    context = {
        'posts':all_data,
        'title': 'Zen of Python'
    }
    return render(request,"blog/home.html", context)

def about(request):
    all_data = Contact.objects.all()
    context ={
        "contacts":all_data
    }
    return render(request, "blog/about.html", context)


def create_post(request):
    if request.method == "GET":
        context = {'form': PostForm()}
        return render(request,"blog/post_form.html",context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"The post is created syccessfully..!")
            return redirect("posts")
        else:
            context= {
                "form": form
            }
            messages.error(request,"Please correct the errors")
            return render(request, "blog/post_form.html", context)

def edit_post(request,id):
    
    post = get_object_or_404(Post, id=id)
    
    if request.method == "GET":
        context = {
            'form': PostForm(instance=post),
            'id': id
        }
        return render(request, "blog/post_form.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,"The post is editted successfully..!")
            return redirect("posts")
        else:
            messages.error(request,"Please correct the errors")
            return render (request,"blog/post_form.html", {'form':form})