import json
import requests
from django.db import models
from tian.settings import GOOGLEMAPS_API


class Building(models.Model):
    stories = models.SmallIntegerField(verbose_name='Этажность', null=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    year = models.DateField(verbose_name='Год постройки')

    def get_address_by_coordinates(self):
        response = requests.get(
           'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}'.
               format(self.lat, self.lng, GOOGLEMAPS_API)).json()
        return json.loads(response)['formatted_address']

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




