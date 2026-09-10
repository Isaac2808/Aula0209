from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

from login.utils import verificar_grupo


# ==========================================================
# REDIRECIONAMENTO DO PAINEL
# ==========================================================

@login_required(login_url='login')
def painel_redirect(request):

    usuario = request.user

    if verificar_grupo(usuario, 'administradores'):
        return redirect('view_administrador')

    if verificar_grupo(usuario, 'diretoria'):
        return redirect('view_diretoria')

    if verificar_grupo(usuario, 'gerencia_geral'):
        return redirect('view_gerencia_geral')

    if verificar_grupo(usuario, 'gerencia'):
        return redirect('view_gerencia')

    if verificar_grupo(usuario, 'supervisao'):
        return redirect('view_supervisao')

    if verificar_grupo(usuario, 'atendente'):
        return redirect('view_atendente')

    if verificar_grupo(usuario, 'caixa'):
        return redirect('view_caixa')

    raise PermissionDenied(
        "Usuário não pertence a nenhum grupo."
    )


# ==========================================================
# PAINEL PRINCIPAL
# ==========================================================

@login_required(login_url='login')
def painel_principal(request):

    usuarios = User.objects.all()

    return render(
        request,
        'painel/home.html',
        {
            'usuarios': usuarios
        }
    )


# ==========================================================
# ADMINISTRADOR
# ==========================================================

@login_required(login_url='login')
def view_administrador(request):

    if not verificar_grupo(
        request.user,
        'administradores'
    ):
        raise PermissionDenied

    return render(
        request,
        'painel/administrador.html'
    )


# ==========================================================
# DIRETORIA
# ==========================================================

@login_required(login_url='login')
def view_diretoria(request):

    if not verificar_grupo(
        request.user,
        'diretoria'
    ):
        raise PermissionDenied

    return render(
        request,
        'painel/diretoria.html'
    )


# ==========================================================
# GERÊNCIA GERAL
# ==========================================================

@login_required(login_url='login')
def view_gerencia_geral(request):

    if not verificar_grupo(
        request.user,
        'gerencia_geral'
    ):
        raise PermissionDenied

    return render(
        request,
        'painel/gerencia_geral.html'
    )


# ==========================================================
# GERÊNCIA
# ==========================================================

@login_required(login_url='login')
def view_gerencia(request):

    if not verificar_grupo(
        request.user,
        'gerencia'
    ):
        raise PermissionDenied

    return render(
        request,
        'painel/gerencia.html'
    )


# ==========================================================
# SUPERVISÃO
# ==========================================================

@login_required(login_url='login')
def view_supervisao(request):

    if not verificar_grupo(
        request.user,
        'supervisao'
    ):
        raise PermissionDenied

    return render(
        request,
        'painel/supervisao.html'
    )


# ==========================================================
# ATENDENTE
# ==========================================================

@login_required(login_url='login')
def view_atendente(request):

    if not verificar_grupo(
        request.user,
        'atendente'
    ):
        raise PermissionDenied

    return render(
        request,
        'painel/atendente.html'
    )


# ==========================================================
# CAIXA
# ==========================================================

@login_required(login_url='login')
def view_caixa(request):

    if not verificar_grupo(
        request.user,
        'caixa'
    ):
        raise PermissionDenied

    return render(
        request,
        'painel/caixa.html'
    )