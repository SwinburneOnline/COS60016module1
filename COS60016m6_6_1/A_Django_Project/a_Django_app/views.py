from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

AUTH_TOKEN = "CMYH"
def authenticate(token):

    if token == AUTH_TOKEN:

        return True

    else:

        return False


def home(request):
    return HttpResponse("I love Python!")

def home(request):
   return HttpResponse("<h1>I love Python!</h1>")

def home(request):
    return render(request, 'home.html')


def contact(request):
    return HttpResponse('contact view')


def contact(request):
    form = ContactForm()
    return render(request, 'form.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        print(name, email)
    form = ContactForm()
    return render(request, 'form.html', {'form': form})

