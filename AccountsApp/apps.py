from django.apps import AppConfig



class AccountsappConfig(AppConfig):
    name = 'AccountsApp'

    def ready(self):
        import AccountsApp.signals
