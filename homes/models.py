from django.db import models
from django.conf import settings


class Homes(models.Model):
    '''
    модель справочника участков
    '''
    class Meta:
        verbose_name = 'Участки'
        verbose_name_plural = 'Участки'
        ordering = ['-section']

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, verbose_name='Владелец участка')
    comment = models.CharField(max_length=100, blank=True, verbose_name='Комментарий (100 символов)')
    street = models.CharField(max_length=150, blank=True, verbose_name='Улица')
    numhome = models.IntegerField(default=0, blank=True, verbose_name='Номер дома')
    section = models.IntegerField(default=0, blank=True, verbose_name='Номер участка')

    def __str__(self):
        return 'участок ' + str(self.section) + ', улица ' + self.street + ', дом ' + str(self.numhome)

    def publish(self):
        self.save()
