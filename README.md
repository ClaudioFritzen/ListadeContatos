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
    bom agora queremos saber se foi