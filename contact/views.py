from django.shortcuts import render

from .models import Contact

# Create your views here.
def index(request):
    contatos = Contact.objects.all().order_by('full_name')
    return render(request, "index.html", {"contatos": contatos})

def addContact(request):
    return render(request, 'new.html')

def editContact(request):
    pass