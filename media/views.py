from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'media.html')

@login_required(login_url='login')
def upload(request):
    if request.method == "POST" and request.FILES['toUpload']:
        file = request.FILES['toUpload']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        #uploaded_file_url = fs.url(filename)
        return render(request, 'upload/upload.html')
    return render(request, 'upload/upload.html')    
