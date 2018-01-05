from django.db import models
from generic.module import CounterBase
from homes.models import Homes
from django.core.exceptions import ValidationError


class CounterW(CounterBase):
    class Meta:
        verbose_name = 'Счетчик воды индивидуальный'
        verbose_name_plural = 'Счетчики воды индивидуальные'
        ordering = ['-month', 'year', 'autor']

    indication = models.FloatField(
        blank=False, default=0, verbose_name='Показание счетчика')

    home = models.ForeignKey(Homes, blank=False, verbose_name='Участок')

    def __str__(self):
        return str(self.created_date
                   ) + ' ' + self.month + ' ' + self.year + ' ' + self.comment

    def publish(self):
        self.save()

    def clean(self):

        if self.indication == 0:
            raise ValidationError('Показание счетчика обязательно должно быть заполнено!')
