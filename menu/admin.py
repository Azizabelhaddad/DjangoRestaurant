from django.contrib import admin

from .models import Pizza, Ingredient, Type

# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ("title", "state", "created")
    list_filter = ("state",)
    # prepopulated_fields = {slug: ("title,")}
    prepopulated_fields = { "slug": ("title",)}
    list_per_page = 10

admin.site.register(Pizza, PizzaAdmin )

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'state',)
    list_filter = ("state",)

    prepopulated_fields = { "slug": ("title",)}
    list_per_page = 10
admin.site.register(Ingredient, IngredientAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'state',)
    list_filter = ("state",)

    prepopulated_fields = { "slug": ("type",)}
    list_per_page = 10
admin.site.register( Type, TypeAdmin)
