from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Esta rota corresponde a /crud/
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Suas demais rotas CRUD:
    path('listagem/', views.listagem, name='listagem'),
    path('selecao/<int:id>/', views.selecao, name='selecao'),
    path('consulta/', views.consulta, name='consulta'),
    path('ordenacao/<str:campo>/', views.ordenacao, name='ordenacao'),
    path('insercao/', views.insercao, name='insercao'),
    path('salvar_insercao/', views.salvar_insercao, name='salvar_insercao'),
    path('edicao/<int:id>/', views.edicao, name='edicao'),
    path('salvar_edicao/', views.salvar_edicao, name='salvar_edicao'),
    path('delecao/<int:id>/', views.delecao, name='delecao'),
    path('salvar_delecao/', views.salvar_delecao, name='salvar_delecao'),
    path('graficos/', views.graficos, name='graficos'),
]
