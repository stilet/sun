from django.db import models
from generic.module import CounterBase
from homes.models import Homes
from counter.models import CounterE
from water.models import CounterW


class Pko(CounterBase):
    class Meta:
        verbose_name = 'Приходный кассовый ордер'
        verbose_name_plural = 'Приходные кассовые ордера'
        ordering = ['-month', 'year', 'autor']

    summ_e = models.FloatField(blank=True, default=0, verbose_name='Сумма оплаты за электричество')

    summ_w = models.FloatField(blank=True, default=0, verbose_name='Сумма оплаты за воду')

    summ_fond = models.FloatField(blank=True, default=0, verbose_name='Сумма оплаты в фонд поселка')

    home = models.ForeignKey(Homes, blank=False, verbose_name='Участок')

    counter_e = models.OneToOneField(CounterE, blank=False, verbose_name='Оплачиваемый счетчик электричества')

    counter_w = models.OneToOneField(CounterW, blank=False, verbose_name='Оплачиваемый счетчик воды')

    def __str__(self):
        return str(self.created_date
                   ) + ' ' + self.month + ' ' + self.year + ' ' + self.comment

    def publish(self):
        self.save()


