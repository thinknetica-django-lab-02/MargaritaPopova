from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models


with open('cities.txt', 'r') as f:
    all_cities = list(f.read().split('\n'))


CITIES_CHOICES = []
for city in all_cities:
    CITIES_CHOICES.append((city, city))


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


class Building(models.Model):
    stories = models.PositiveSmallIntegerField(verbose_name='Этажность', null=True, blank=True)
    lat = models.FloatField(verbose_name='Широта', validators=[validate_lat], blank=True)
    lng = models.FloatField(verbose_name='Долгота', validators=[validate_lng], blank=True)
    city = models.CharField(verbose_name='Населенный пункт', choices=CITIES_CHOICES, default='', max_length=200)
    street = models.CharField(verbose_name='Улица', default='', max_length=200)
    number = models.PositiveSmallIntegerField(verbose_name='Дом', default=0)
    year = models.PositiveSmallIntegerField(verbose_name='Год постройки', null=True, blank=True)

    def __str__(self):
        if not (self.street or self.city):
            return f'Building {self.id}'
        return f'{self.city}, ул. {self.street}, д. {self.number}'


class Apartment(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='Адрес')
    story = models.SmallIntegerField(verbose_name='Этаж', null=True)
    rooms = models.SmallIntegerField(verbose_name='Количество комнат', null=True)
    price = models.FloatField(verbose_name='Цена общая')
    area = models.FloatField(verbose_name='Площадь')
    number = models.PositiveSmallIntegerField(verbose_name='Номер квартиры')

    def __str__(self):
        return f'Квартира в {self.building.__str__()}'




