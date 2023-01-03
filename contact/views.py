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
        relationship = request.POST.get('relationship')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        email = request.POST.get('email')


        print([fullname, relationship,phone_number, address, email])
        contato = Contact(
            full_name = fullname,
            relationship = relationship,
            phone_number = phone_number,
            address = address,
            email = email
        )
        contato.save()
        return render(request, 'index.html')

def editContact(request):
    pass