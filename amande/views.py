from django.shortcuts import render

from .models import MenuCategory, MenuItem


def home(request):

    categories = MenuCategory.objects.all()

    menu_items = MenuItem.objects.select_related(
        "category"
    ).all()

    return render(
        request,
        "index.html",
        {
            "categories": categories,
            "menu_items": menu_items,
        }
    )