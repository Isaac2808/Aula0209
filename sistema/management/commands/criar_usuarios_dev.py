from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):

    help = 'Cria usuários de teste e associa aos grupos'

    def handle(self, *args, **options):

        # Grupos e nomes dos usuários
        usuarios = [
            {
                'grupo': 'administradores',
                'nome': 'Administrador',
            },
            {
                'grupo': 'diretoria',
                'nome': 'Diretoria',
            },
            {
                'grupo': 'gerencia_geral',
                'nome': 'Gerência Geral',
            },
            {
                'grupo': 'gerencia',
                'nome': 'Gerência',
            },
            {
                'grupo': 'supervisao',
                'nome': 'Supervisão',
            },
            {
                'grupo': 'atendente',
                'nome': 'Atendente',
            },
            {
                'grupo': 'caixa',
                'nome': 'Caixa',
            },
        ]

        senha_padrao = 'dev12345'

        for dados in usuarios:

            nome_grupo = dados['grupo']
            nome_usuario = dados['nome']

            username = f'user_{nome_grupo}'
            email = f'{nome_grupo}@dev.com'

            # ==========================================
            # CRIA O GRUPO CASO ELE NÃO EXISTA
            # ==========================================

            grupo, grupo_criado = Group.objects.get_or_create(
                name=nome_grupo
            )

            if grupo_criado:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Grupo criado: {nome_grupo}'
                    )
                )

            # ==========================================
            # CRIA O USUÁRIO CASO NÃO EXISTA
            # ==========================================

            user, usuario_criado = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': nome_usuario,
                    'email': email,
                    'is_staff': False,
                    'is_active': True,
                }
            )

            # ==========================================
            # SE O USUÁRIO JÁ EXISTIR
            # ATUALIZA OS DADOS
            # ==========================================

            if not usuario_criado:

                user.first_name = nome_usuario
                user.email = email
                user.is_active = True
                user.save()

                self.stdout.write(
                    self.style.WARNING(
                        f'Usuário "{username}" já existe.'
                    )
                )

            else:

                # Define a senha somente na criação
                user.set_password(senha_padrao)
                user.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Usuário "{username}" criado.'
                    )
                )

            # ==========================================
            # ASSOCIA O USUÁRIO AO GRUPO
            # ==========================================

            user.groups.add(grupo)

            self.stdout.write(
                self.style.SUCCESS(
                    f'Grupo "{nome_grupo}" associado ao usuário "{username}".'
                )
            )

            self.stdout.write(
                f'   E-mail: {email}'
            )

            self.stdout.write(
                f'   Senha: {senha_padrao}'
            )

            self.stdout.write('')

        # ==========================================
        # FINAL
        # ==========================================

        self.stdout.write(
            self.style.SUCCESS(
                'Todos os usuários de desenvolvimento foram processados!'
            )
        )