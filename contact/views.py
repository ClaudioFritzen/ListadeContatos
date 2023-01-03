from django.shortcuts import render, HttpResponse

from .models import Contact

# Create your views here.
def index(request):
    contatos = Contact.objects.all().order_by('full_name')
    return render(request, "index.html", {"contatos": contatos})

def addContact(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    elif request.method == 'POST':
        fullname = request.POST.get('fullname')
        print(fullname)
        return HttpResponse("post")

def save(request):
    pass

def editContact(request):
    pass