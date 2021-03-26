from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models


def validate_lat(lat):
    if not -90 <= lat <= 90:
        raise ValidationError(
            _('%(lat)s must be between -90 and 90 degrees'),
            params={'lat': lat},
        )


def validate_lng(lng):
    if not -180 <= lng <= 180:
        raise ValidationError(
            _('%(lng)s must be between -180 and 180 degrees'),
            params={'lng': lng},
        )


class Location(models.Model):
    name = models.CharField(verbose_name='Населенный пункт', blank=False, max_length=200)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(verbose_name='Улица', max_length=128)


class Building(models.Model):
    stories = models.PositiveSmallIntegerField(verbose_name='Этажность', null=True, blank=True)
    lat = models.FloatField(verbose_name='Широта', validators=[validate_lat], blank=True, null=True)
    lng = models.FloatField(verbose_name='Долгота', validators=[validate_lng], blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='buildings')
    street = models.ForeignKey(Street, verbose_name='Улица', related_name='buildings', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField(verbose_name='Дом')
    year = models.PositiveSmallIntegerField(verbose_name='Год постройки', null=True, blank=True)

    def __str__(self):
        if not (self.street or self.location):
            return f'Building {self.id}'
        return f'{self.location}, ул. {self.street}, д. {self.number}'


class Apartment(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='Адрес')
    story = models.PositiveSmallIntegerField(verbose_name='Этаж', null=True)
    rooms = models.PositiveSmallIntegerField(verbose_name='Количество комнат', null=True)
    price = models.FloatField(verbose_name='Цена общая')
    area = models.FloatField(verbose_name='Площадь')
    number = models.PositiveSmallIntegerField(verbose_name='Номер квартиры')

    def __str__(self):
        return f'Квартира в {self.building.__str__()}'






