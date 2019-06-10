from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from testapp.models import Document,ResumeDocument
from testapp.forms import DocumentForm

def HM(request):
    return  render(request,'testapp/hm.html')
def home(request):
    documents = Document.objects.all()
    pdocuments=ResumeDocument.objects.all()
    return render(request, 'testapp/home.html', { 'documents': documents ,'pdocuments':pdocuments})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'testapp/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'testapp/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'testapp/model_form_upload.html', {
        'form': form
    })
