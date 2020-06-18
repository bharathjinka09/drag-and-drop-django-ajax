from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "drag_and_drop_ajax_lists_with_django.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import drag_and_drop_ajax_lists_with_django.users.signals  # noqa F401
        except ImportError:
            pass
