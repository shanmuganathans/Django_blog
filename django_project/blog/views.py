from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Contact
from .forms import PostForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.core.mail import send_mail

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .signals import custom_signal

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

@login_required
def home(request):
    logger.warning('Homepage was accessed')
    all_data = Post.objects.all()
    context = {
        'posts':all_data,
        'title': 'Zen of Python'
    }
    return render(request,"blog/home.html", context)

@login_required
def about(request):
    all_data = Contact.objects.all()
    context ={
        "contacts":all_data
    }
    custom_signal.send(sender=None, instance = all_data)
    return render(request, "blog/about.html", context)

@login_required
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
        
@login_required
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
        
@login_required       
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    context ={ 'post': post }
    
    if request.method == "GET":
        return render(request, "blog/post_confirm_delete.html",context)
    elif request.method == "POST":
        post.delete()
        messages.success(request,"The post is deleted successfully..!")
        return redirect("posts")
    
def send_email_view(request):
    # Send email
    send_mail(
        'Subject',  # Subject of the email
        'Message body',  # Body of the email
        'Testing@gmail.com.com',  # Sender's email address
        ['to_mail_id@example.com'],  # List of recipient email addresses
        fail_silently=False,  # Set to True to suppress exceptions (optional)
    )
    return HttpResponse('Email sent successfully!')


def test_pagination(request):
    object_list = Contact.objects.all()
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 2) # 6 employees per page


    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'blog/pagination.html', {'page_obj': page_obj})

class PaginationTest(ListView):
    model = Contact
    context_object_name = 'contact'
    paginate_by = 2
    template_name = 'blog/pagination.html'
