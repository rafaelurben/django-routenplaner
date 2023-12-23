from django.contrib import admin

from .models import Route, Ort

# Register your models here.


class RoutenAdminOrteInline(admin.TabularInline):
    model = Ort
    extra = 0

    readonly_fields = ("html_link",)
    fields = ("pos", "aktiv", "adresse", "name", "html_link")
    ordering = ("pos", "name")


@admin.register(Route)
class RoutenAdmin(admin.ModelAdmin):
    list_display = ("name",)

    inlines = (RoutenAdminOrteInline,)
