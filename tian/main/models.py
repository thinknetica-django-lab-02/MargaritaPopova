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


class Building(models.Model):
    stories = models.SmallIntegerField(verbose_name='Этажность', null=True, blank=True)
    lat = models.FloatField(verbose_name='Широта', validators=[validate_lat])
    lng = models.FloatField(verbose_name='Долгота', validators=[validate_lng])
    year = models.SmallIntegerField(verbose_name='Год постройки', null=True, blank=True)


    def get_address_by_coordinates(self):
        from geopy.geocoders import Nominatim

        geolocator = Nominatim(user_agent="tian")
        location = geolocator.reverse([self.lat, self.lng], timeout=10)
        return location.address

    def __str__(self):
        return self.get_address_by_coordinates()


class Apartment(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='Адрес')
    story = models.SmallIntegerField(verbose_name='Этаж', null=True)
    rooms = models.SmallIntegerField(verbose_name='Количество комнат', null=True)
    price = models.FloatField(verbose_name='Цена общая')
    area = models.FloatField(verbose_name='Площадь')

    def __str__(self):
        return f'Квартира в {self.building.__str__()}'




