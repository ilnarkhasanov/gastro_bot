from django.contrib import admin
from clinics.models import Clinic


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ("name", "booking_url", "maps_app_url")
    list_display_links = ("booking_url", "maps_app_url")
    list_editable = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    fieldsets = (
        (None, {"fields": ("name", "booking_url", "maps_app_url")}),
    )

