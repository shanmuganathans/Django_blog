from django.shortcuts import render, redirect
from .forms import UploadFileForm

# Create your views here.
def uploda_file(request):
    if request.method == "GET":
        context = {
            "form": UploadFileForm()
        }
        return render(request,"file_upload_app/upload.html", context)
    elif request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload_success")
        else:
            form = UploadFileForm()
            context={
                "form": form
            }
            return render(request,"file_upload_app/upload.html", context)
        
def upload_success(request):
    return render(request, "file_upload_app/upload_success.html")