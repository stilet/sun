from django.db import models
from generic.module import CounterBase
from homes.models import Homes
from django.core.exceptions import ValidationError


class CounterE(CounterBase):
    """
     FIXME: 1. Представление документа на самое удачное - по комментарию
     надо добиться представления по месяцу, году, номеру участка , и автору
     FIXME: при создании документа значение по умолчанию автор не подставляется
     FIXME: при попытке записи надо проверять - есть ли уже документ с таким месяцем и годом - если есть
     то надо редактировать тот документ, а не создавать новый
    """

    class Meta:
        verbose_name = 'Счетчик электроэнергии индивидуальный'
        verbose_name_plural = 'Счетчики электроэнергии индивидуальные'
        ordering = ['-month', 'year', 'autor']

    indication_day = models.FloatField(
        blank=False, verbose_name='Показание дневной тариф'
    )
    indication_night = models.FloatField(
        blank=False, verbose_name='Показание ночной тариф')

    home = models.ForeignKey(Homes, blank=False, verbose_name='Участок')

    def __str__(self):
        return '№ ' + str(self.id) + ' от ' + str(self.created_date) + ' за ' + self.month + ' ' + self.year

    def publish(self):
        self.save()

    def clean(self):

        if self.indication_day == 0:
            raise ValidationError('Показание счетчика обязательно должно быть заполнено!')

