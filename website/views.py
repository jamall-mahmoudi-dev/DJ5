from django.shortcuts import render
from website.forms import NameForm
# Create your views here.
# Mahdis


def test(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        status = request.POST.get('status')
        description = request.POST.get('description')
        print(name, email, subject, message, status, description)
    form = NameForm()
        
    return render(request, 'website/test.html', {'form': form})

def test_do(request):
    return render(request, 'website/test_do.html')

def nginx(request):
    return render(request,'website/nginx.html')

def about(request):
    return render(request, 'website/about.html')

def index(request):
    return render(request, 'website/index.html')

def contact(request):
    return render(request, 'website/contact.html')
    