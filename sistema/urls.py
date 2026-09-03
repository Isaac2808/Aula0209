"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from app import views as app_views
from cadastro import views as cadastro_views
from login import views as login_views
from carrinho import views as carrinho_views
from painel import views as painel_views
from c_produto import views as c_produto_views

urlpatterns = [
 path('admin/', admin.site.urls),
 path('app/', app_views.app, name='app'),
 path('cadastro/', cadastro_views.cadastro, name='cadastro'),
 path('login/', login_views.login_view, name='login'),
 path('carrinho/', carrinho_views.carrinho, name='carrinho'),
 path('painel/', painel_views.painel, name='painel'),
 path('c_produto/', c_produto_views.c_produto, name='c_produto'),
 
]
