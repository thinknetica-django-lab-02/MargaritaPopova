from django.core.exceptions import ValidationError
from django.db import models


class Building(models.Model):
    stories = models.SmallIntegerField(verbose_name='Этажность', null=True)
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')
    year = models.SmallIntegerField(verbose_name='Год постройки')

    def clean(self):
        super().clean()
        if not -90 <= self.lat <= 90 and -180 <= self.lng <= 180:
            raise ValidationError('incorrect coordinates')

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
        return self.building




