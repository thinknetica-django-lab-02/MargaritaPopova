from django.contrib import admin
from main.models import Building, Apartment
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from django.db import models
from ckeditor.widgets import CKEditorWidget


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


class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.unregister(FlatPage)
admin.site.register(Apartment)
admin.site.register(FlatPage, FlatPageAdmin)
