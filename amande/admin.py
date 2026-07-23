from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import AdminSite

from .models import MenuCategory, MenuItem



@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):

    list_display = [
        "name",
    ]

    search_fields = [
        "name",
    ]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = [
        "image_preview",
        "name",
        "category",
        "price",
    ]

    list_filter = [
        "category",
    ]

    search_fields = [
        "name",
    ]

    readonly_fields = [
        "image_preview",
    ]

    def image_preview(self, obj):

        if obj.image:

            return format_html(
                '<img src="{}" width="80" height="80" '
                'style="object-fit:cover;border-radius:10px;">',
                obj.image.url
            )

        return "-"

    image_preview.short_description = "Rasm"

class Media:

    js = (
        "admin/js/uzbek_admin.js",
    )



class UzbekAdminSite(AdminSite):

    class Media:

        js = (
            "admin/js/uzbek_admin.js",
        )