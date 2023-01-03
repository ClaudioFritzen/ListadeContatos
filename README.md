# Esse projeto consiste em fazer uma agenda telefonica.

# funcionalidades principais
    1. Criar um novo contato
    2. Listar todos os contatos
    2. Edita-lo
    3. Deletar o contato

# Primeiro criando um contato
    Temos um contato salvo no banco pelo adm.

# Agora quero mostrar todos os meus contatos do banco

    1. Da fução views.py na index vamos intanciar uma variavel e fazer a importação do models contatos

    from .models import Contatos

    faremos um filtro em nosso banco de dados
    e traremos todos os nosso contatos salvos 
    no banco.

    dentro do return, retornaremos a tela inicial
    com uma { "contatos": contatos}

    def index(request):
    contatos = Contact.objects.all()
    return render(request, "index.html", {"contatos": contatos})

    e assim liberamos os prints do django dentro do 
    html.

    para acessar as propriedados do banco de dados em nosso html
    utilizaremos a chaves {}, e o nome passado dentro das {}
    na função. 
    Utilizaremos o ponto . para chamar o nome do item do models.
    Quero pegar apenas o nome da pessoa.
    Entao ficará assim. 
    {contatos.full_name}

    Então utilizando o for, trazeremos todos de uma vez só e 
    deixaremos dinaco.

    {for contato in contatos}
        {{contato.full_name}}
    {endfor}

    Com isso podemos passar todos o que queremos para o front de 
    forma dinamica.


# Adicionar um contato.
# Adicionar um contato e mostra a lista de contatos 
# fazer as validações.


# Como queremos fazer.. 
o botao do +, abriremos um formulario com os campos desejados.
e faremos a conexão com o nosso banco e adicionaremos ao banco
e voltaremos para pagina index

e organizemos os contatos por order alfabetica

# Passo 1
no form dentro do action coloca a tag do django de url
dentro com o nome dado la na url. no meu caso o name='index'. Então passemos
form action="{% url 'index' %}" method="POST">
e quando a pessoa clicar em salvar será redirecionada
a pagina inicial.

# Passo 2 
    Vamos pegar os dados enviados ao formulário,
para todos os campos iremos declarar uma variavél e
pegaremos todos os campos.
    Na pagina html na em cada input tem um name utilizaremos esse name para pegar os dados do input
    
    como pegar um dado enviado do formulario, utilizaremos o metodo request.POST.get(nome do input)
    pegarNome = request.POST.get('fullname')
    para fazer um teste e ver se esta a funcionando 
    fazemos um print da variavel
    print(pegarNome)

    fazemos isso para todos os dados do formulário

# Passo 3 Salvar no banco
    para salvar no banco criaremos uma variavel e colocaremos como atributo a models e abriremos (    ) e dentr dele colocaremos dois paramentros para cada input, sendo o primeiro parametro é o nome dado na models do objeto, e a direita o nome da variavel recebida no request.POST....
    exemplo completo

    contato = Contact(
            full_name = fullname,
            relationship = relationship,
            phone_number = phone_number,
            address = address,
            email = email
        )
    e fora do objeto daremos save em contato, nome dado a minha variavel acima

    contato.save()

    se tudo correr bem estará salvo no banco

