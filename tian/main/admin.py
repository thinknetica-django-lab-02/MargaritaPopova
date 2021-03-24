from django.contrib import admin
from main.models import Building, Apartment


class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 1


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('stories', 'year')}),
        ('Координаты', {'fields': ('lng', 'lat',)}),
    ]
    inlines = [ApartmentInline]


admin.site.register(Apartment)
