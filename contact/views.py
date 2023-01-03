from django.shortcuts import render

from .models import Contact

# Create your views here.
def index(request):
    contatos = Contact.objects.all()
    return render(request, "index.html", {"contatos": contatos})
    return render(request, 'index.html')

def addContact(request):
    return render(request, 'new.html')

def editContact(request):
    pass