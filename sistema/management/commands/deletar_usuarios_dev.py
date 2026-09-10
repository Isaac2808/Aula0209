from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    help = 'Deleta usuários de teste do ambiente de desenvolvimento'

    def add_arguments(self, parser):

        parser.add_argument(
            '--all',
            action='store_true',
            help='Deleta todos os usuários. CUIDADO!',
        )

        parser.add_argument(
            '--username',
            type=str,
            help='Deleta um usuário específico pelo username',
        )

    def handle(self, *args, **options):

        # ==========================================
        # DELETAR USUÁRIO ESPECÍFICO
        # ==========================================

        if options['username']:

            username = options['username']

            try:

                user = User.objects.get(
                    username=username
                )

                user.delete()

                self.stdout.write(
                    self.style.SUCCESS(
                        f'✓ Usuário "{username}" deletado com sucesso.'
                    )
                )

            except User.DoesNotExist:

                self.stdout.write(
                    self.style.ERROR(
                        f'✗ Usuário "{username}" não encontrado.'
                    )
                )

            return


        # ==========================================
        # DELETAR TODOS OS USUÁRIOS
        # ==========================================

        if options['all']:

            self.stdout.write(
                self.style.WARNING(
                    '\n⚠ ATENÇÃO!'
                )
            )

            self.stdout.write(
                'Você está prestes a DELETAR TODOS os usuários.'
            )

            self.stdout.write(
                'Isso inclui administradores e usuários reais.\n'
            )

            confirmacao = input(
                'Digite "SIM" para continuar: '
            )

            if confirmacao != 'SIM':

                self.stdout.write(
                    self.style.WARNING(
                        'Operação cancelada.'
                    )
                )

                return

            count = User.objects.count()

            User.objects.all().delete()

            self.stdout.write(
                self.style.SUCCESS(
                    f'✓ {count} usuário(s) deletado(s) com sucesso.'
                )
            )

            return


        # ==========================================
        # DELETAR USUÁRIOS DE DESENVOLVIMENTO
        # ==========================================

        nomes_grupos = [
            'administradores',
            'diretoria',
            'gerencia_geral',
            'gerencia',
            'supervisao',
            'atendente',
            'caixa',
        ]

        count = 0

        for nome in nomes_grupos:

            username = f'user_{nome}'

            try:

                user = User.objects.get(
                    username=username
                )

                user.delete()

                count += 1

                self.stdout.write(
                    self.style.SUCCESS(
                        f'✓ Usuário "{username}" deletado.'
                    )
                )

            except User.DoesNotExist:

                self.stdout.write(
                    self.style.WARNING(
                        f'○ Usuário "{username}" não encontrado.'
                    )
                )


        # ==========================================
        # RESULTADO
        # ==========================================

        self.stdout.write('')

        self.stdout.write(
            self.style.SUCCESS(
                f'✓ Total: {count} usuário(s) '
                f'de desenvolvimento deletado(s).'
            )
        )