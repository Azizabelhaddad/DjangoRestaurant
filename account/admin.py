from .models import Profile
from django.contrib import admin

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'state',)
    list_filter = ("state",)

    prepopulated_fields = { "slug": ("username",)}
    list_per_page = 10
admin.site.register(Profile, ProfileAdmin)