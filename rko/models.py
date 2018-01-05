from django.db import models
from generic.module import CounterBase


class Rko(CounterBase):
    class Meta:
        verbose_name = 'Расходный кассовый ордер'
        verbose_name_plural = 'Расходный кассовый ордер'
        ordering = ['-month', 'year', 'autor']

    summ_fond = models.FloatField(
        blank=True, default=0, verbose_name='Сумма оплаты из фонда поселка')


    def __str__(self):
        return str(self.created_date
                   ) + ' ' + self.month + ' ' + self.year + ' ' + self.comment

    def publish(self):
        self.save()
