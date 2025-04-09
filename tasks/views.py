from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def hello_world(request):
#     return render(request, 'signup.html', {''
#     'form':UserCreationForm
#     })

def home(request):
    return render(request, 'home.html')

def signup(request):
    if(request.method == 'GET'):
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        return render(request, 'home.html')
    
