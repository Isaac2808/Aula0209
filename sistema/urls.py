from django.contrib import admin
from django.urls import path

from app import views as app_views
from cadastro import views as cadastro_views
from login import views as login_views
from carrinho import views as carrinho_views
from painel import views as painel_views
from c_produto import views as c_produto_views


urlpatterns = [

    # Administração
    path('admin/', admin.site.urls),

    # Loja
    path('app/', app_views.app, name='app'),

    # Cadastro
    path('cadastro/', cadastro_views.cadastro, name='cadastro'),

    # Login
    path('login/', login_views.login_view, name='login'),

    # Carrinho
    path('carrinho/', carrinho_views.carrinho, name='carrinho'),

    # Produtos
    path('c_produto/', c_produto_views.c_produto, name='c_produto'),

    # ==================================================
    # PAINEL
    # ==================================================

    # Entrada do painel.
    # Verifica o grupo e redireciona para o painel correto.
    path('painel/',painel_views.painel_redirect,name='painel'),

    # Administrador
    path('painel/administrador/',painel_views.view_administrador,name='view_administrador'),

    # Diretoria
    path('painel/diretoria/',painel_views.view_diretoria,name='view_diretoria'),

    # Gerência Geral
    path('painel/gerencia-geral/',painel_views.view_gerencia_geral,name='view_gerencia_geral'),

    # Gerência
    path('painel/gerencia/',painel_views.view_gerencia,name='view_gerencia'),

    # Supervisão
    path('painel/supervisao/',painel_views.view_supervisao,name='view_supervisao'),

    # Atendente
    path('painel/atendente/',painel_views.view_atendente,name='view_atendente'),

    # Caixa
    path('painel/caixa/',painel_views.view_caixa,name='view_caixa'),
]
