from django.shortcuts import render, HttpResponse, redirect

from .models import Contact

# importações pra usar mensagens
from django.contrib.messages import constants as messages
from django.contrib import messages

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

        if len(fullname.strip()) == 0 or (len(phone_number.strip()) == 0):
            messages.add_message(request, messages.ERROR, 'Não pode salvar vazio!')
            return redirect(f'/add_contact')
            return HttpResponse('Erro, Nome e numero são obrigatórios')
            print([fullname, relationship,phone_number, address, email])

        if len(fullname.strip()) <= 5:
            return HttpResponse('Nome precisa ter mais de 5')
        
        if len(phone_number.strip()) <= 5:
            return HttpResponse('Numero tem menos que 5')
            print (type(phone_number))
        else:
            return HttpResponse('Salvo com sucesso')
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