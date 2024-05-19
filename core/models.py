from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import (models)


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Updated Date"
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Created Date"
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name Test",
        help_text='This is the variable of the setting.'
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Description"
    )
    parameter = models.CharField(
        default='',
        max_length=512,
        blank=True,
        verbose_name="Parameter"
    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        app_label = 'core'
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)

