from django.db import models
from django.utils.translation import ugettext_lazy as _

from fitclip.shop.models.category import Category


class Section(models.Model):
    name = models.CharField(
        max_length=10,
        verbose_name=_("상세 분류 이름"),
        help_text=_("카테고리내의 상세 분류 이름입니다.")
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_("카테고리")
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('상세 분류')
        verbose_name_plural = _('상세 분류')