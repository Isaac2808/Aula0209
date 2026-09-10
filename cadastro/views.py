from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
import uuid


def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return render(request, "cadastro.html")

        if len(senha) < 8:
            messages.error(
                request,
                "A senha deve ter pelo menos 8 caracteres."
            )
            return render(request, "cadastro.html")

        if User.objects.filter(email=email).exists():
            messages.error(
                request,
                "Este e-mail já está cadastrado."
            )
            return render(request, "cadastro.html")

        username_unico = uuid.uuid4().hex[:30]

        user = User.objects.create_user(
            username=username_unico,
            email=email,
            password=senha,
            first_name=nome,
            is_active=False,
        )

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        relative_link = reverse(
            "ativar_conta",
            kwargs={
                "uidb64": uid,
                "token": token
            }
        )

        domain = get_current_site(request).domain
        activation_url = f"http://{domain}{relative_link}"

        assunto = "Confirme seu e-mail de cadastro"

        mensagem = (
            f"Olá, {user.first_name}!\n\n"
            f"Por favor, clique no link abaixo para ativar sua conta:\n\n"
            f"{activation_url}\n\n"
            f"Se você não solicitou este cadastro, ignore este e-mail."
        )

        send_mail(
            assunto,
            mensagem,
            None,
            [user.email],
            fail_silently=False
        )

        messages.success(
            request,
            "Cadastro realizado! Enviamos um link de ativação para o seu e-mail."
        )

        return redirect("login")

    return render(request, "cadastro.html")

# Create your views here.
