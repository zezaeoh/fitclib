from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ShopConfig(AppConfig):
    name = 'fitclip.shop'
    verbose_name = _('쇼핑몰 관리')
