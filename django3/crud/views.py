from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


@login_required
@csrf_protect
def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
           
            login(request, user)
          
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    """
    Tela principal, exibindo a listagem de pessoas.
    Essa view corresponde à URL /crud/
    """
    titulo = 'Listagem de Pessoas'
    pessoas = Pessoa.objects.all()
    return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})



@login_required
def listagem(request):
    titulo = 'Listagem de Pessoas'
    pessoas = Pessoa.objects.all()
    return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})
@login_required
def selecao(request, id):
    titulo = 'Listagem de Pessoas'
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'listagem.html', {'titulo': titulo, 'pessoa': pessoa})
@login_required    
@csrf_protect
def consulta(request):
    consulta_valor = request.POST.get('consulta')
    campo = request.POST.get('campo')
    if campo == 'nome':
        pessoas = Pessoa.objects.filter(nome__contains=consulta_valor)
    elif campo == 'idade':
        pessoas = Pessoa.objects.filter(idade__contains=consulta_valor)
    elif campo == 'sexo':
        pessoas = Pessoa.objects.filter(sexo__contains=consulta_valor)
    elif campo == 'salario':
        pessoas = Pessoa.objects.filter(salario__contains=consulta_valor)
    else:
        pessoas = Pessoa.objects.all()
    titulo = 'Listagem de Pessoas'
    return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

_campo = ''
@login_required
def ordenacao(request, campo):
    titulo = 'Listagem de Pessoas'
    global _campo
    # Converte o campo para minúsculas para garantir correspondência com o modelo
    campo_model = campo.lower()
    if campo_model == _campo:
        # Ordena de forma decrescente
        pessoas = Pessoa.objects.all().order_by(campo_model).reverse()
        _campo = ''
    else:
        pessoas = Pessoa.objects.all().order_by(campo_model)
        _campo = campo_model
    return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

@login_required  
def insercao(request):
    titulo = 'Inserção de Pessoa'
    return render(request, 'insercao.html', {'titulo': titulo})

@login_required
@csrf_protect
def salvar_insercao(request):
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    sexo = request.POST.get('sexo')
    salario = request.POST.get('salario')
    salario = salario.replace(',', '.')
    
    objeto = Pessoa(
        nome=nome,
        idade=idade,
        sexo=sexo,
        salario=salario
    )
    objeto.save()  # Salva o registro

    titulo = 'Listagem de Pessoas'
    pessoas = Pessoa.objects.all()  # Recupera a lista atualizada
    return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})
@login_required
def edicao(request, id):
    titulo = 'Edição de Pessoa'
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'edicao.html', {'titulo': titulo, 'pessoa': pessoa})
@login_required
@csrf_protect
def salvar_edicao(request):
    id = request.POST.get('id')
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    sexo = request.POST.get('sexo')
    salario = request.POST.get('salario')
    salario = salario.replace(',', '.')
    
    Pessoa.objects.filter(id=id).update(
        nome=nome,
        idade=idade,
        sexo=sexo,
        salario=salario
    )
    
    titulo = 'Listagem de Pessoas'
    pessoas = Pessoa.objects.all()
    return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})
@login_required
def delecao(request, id):
    titulo = 'Deleção de Pessoa'
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'delecao.html', {'titulo': titulo, 'pessoa': pessoa})
@login_required
@csrf_protect
def salvar_delecao(request):
    id = request.POST.get('id')
    Pessoa.objects.get(id=id).delete()
    
    titulo = 'Listagem de Pessoas'
    pessoas = Pessoa.objects.all()
    return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})
@login_required
def graficos(request):
    titulo = 'Gráficos Estatísticos por Sexo'
    pessoasM = Pessoa.objects.filter(sexo='M')
    pessoasF = Pessoa.objects.filter(sexo='F')
    
    # Cálculo da média salarial para homens
    salarioM = 0
    for m in pessoasM:
        salarioM += m.salario
    if len(pessoasM) > 0:
        salarioM = salarioM / len(pessoasM)
    
    # Cálculo da média salarial para mulheres
    salarioF = 0
    for f in pessoasF:
        salarioF += f.salario
    if len(pessoasF) > 0:
        salarioF = salarioF / len(pessoasF)
    
    # Cálculo da média de idade para homens
    idadeM = 0
    for m in pessoasM:
        idadeM += m.idade
    if len(pessoasM) > 0:
        idadeM = idadeM / len(pessoasM)
    
    # Cálculo da média de idade para mulheres
    idadeF = 0
    for f in pessoasF:
        idadeF += f.idade
    if len(pessoasF) > 0:
        idadeF = idadeF / len(pessoasF)
    
    return render(request, 'graficos.html', {
        'titulo': titulo,
        'salarioM': salarioM,
        'salarioF': salarioF,
        'idadeM': idadeM,
        'idadeF': idadeF
    })
