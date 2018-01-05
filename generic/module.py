from django.utils import timezone
from datetime import date
from django.db import models
from django.conf import settings


class TimeMonth():

    def getmonth():

        MonthInCounter = (
            ('Январь', 'Январь'),
            ('Февраль', 'Февраль'),
            ('Март', 'Март'),
            ('Апрель', 'Апрель'),
            ('Май', 'Май'),
            ('Июнь', 'Июнь'),
            ('Июль', 'Июль'),
            ('Август', 'Август'),
            ('Сентябрь', 'Сентябрь'),
            ('Октябрь', 'Октябрь'),
            ('Ноябрь', 'Ноябрь'),
            ('Декабрь', 'Декабрь'),)

        return MonthInCounter

    def getyear():

        YearInCounter = (
            ('2017', '2017'),
            ('2018', '2018'),
            ('2019', '2019'),
            ('2020', '2020'),)

        return YearInCounter

    def getstrdate(monthyear):
        '''
        функция возвращает строковое представление месяца и года для подстановки значения по умолчанию в моделях
        monthyear - строка месяц или год. В зависимости от этого возвращается либо текущий месяц либо текущий год
        '''
        MonthInCounter = {
            1: 'Январь',
            2: 'Февраль',
            3: 'Март',
            4: 'Апрель',
            5: 'Май',
            6: 'Июнь',
            7: 'Июль',
            8: 'Август',
            9: 'Сентябрь',
            10: 'Октябрь',
            11: 'Ноябрь',
            12: 'Декабрь'
        }

        now_date = date.today()  # Текущая дата (без времени)
        cur_year = now_date.year  # Год текущий
        cur_month = now_date.month  # Месяц текущий

        if (monthyear == 'месяц'):
            defdate = MonthInCounter[cur_month]
        else:
            defdate = str(cur_year)

        return defdate


class CounterBase(models.Model):
    class Meta:
        abstract = True

    autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор документа')
    created_date = models.DateField(
        default=timezone.now, verbose_name='Дата создания')
    month = models.CharField(
        max_length=8,
        choices=TimeMonth.getmonth(),
        default=TimeMonth.getstrdate('месяц'),
        verbose_name='Месяц снятия показаний')
    year = models.CharField(
        max_length=4,
        choices=TimeMonth.getyear(),
        default=TimeMonth.getstrdate('год'),
        verbose_name='Год снятия показаний')
    comment = models.CharField(
        max_length=100, blank=True, verbose_name='Комментарий (100 символов)')


class GetTarif():

    def getelectroday(self):
        return 3

    def getelectronaith(self):
        return 2

    def getwater(self):
        return 56

