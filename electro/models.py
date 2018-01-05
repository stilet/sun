from django.db import models
from generic.module import CounterBase
from django.core.exceptions import ValidationError


# Модель счетчика электричества общего.
class CommonE(CounterBase):
    class Meta:
        verbose_name = 'Счетчик электроэнергии коттеджный'
        verbose_name_plural = 'Счетчик электроэнергии коттеджный'
        ordering = ['-month', 'year', 'autor']

    indication_day = models.FloatField(
        blank=False, verbose_name='Показание дневной тариф'
    )
    indication_night = models.FloatField(
        blank=False, verbose_name='Показание ночной тариф')

    def __str__(self):
        return str(self.created_date
                   ) + ' ' + self.month + ' ' + self.year + ' ' + self.comment

    def publish(self):
        self.save()

    def clean(self):

        if self.indication_day == 0:
            raise ValidationError('Дневной тариф обязательно должен быть заполнен!')
        if self.indication_night == 0:
            raise ValidationError('Дневной тариф обязательно должен быть заполнен!')


# Модель счетчика электричества общего.
class WaterE(CounterBase):
    class Meta:
        verbose_name = 'Счетчик воды коттеджный'
        verbose_name_plural = 'Счетчик воды коттеджный'
        ordering = ['-month', 'year', 'autor']

    indication = models.FloatField(
        blank=False, verbose_name='Расход воды общий (куб. м.)'
    )

    def __str__(self):
        return str(self.created_date
                   ) + ' ' + self.month + ' ' + self.year + ' ' + self.comment

    def publish(self):
        self.save()

    def clean(self):

        if self.indication == 0:
            raise ValidationError('Показание счетчика обязательно должно быть заполнено!')

