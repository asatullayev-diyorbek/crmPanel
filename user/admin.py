from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .models import (
    User
)
from unfold.admin import ModelAdmin

# ------------------------
# USER ADMIN CUSTOMIZATION
# ------------------------
@admin.register(User)
class CustomUserAdmin(ModelAdmin):
    # qo'shimcha method: thumbnail
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="40" height="40" style="border-radius:50%;" />', obj.image.url)
        return "No Image"
    image_tag.short_description = "Rasm"
    
    # admin panelda ko'rinadigan ustunlar
    list_display = ("id", "image_tag", "username", "first_name", "last_name", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_superuser", "is_active")
    list_display_links = ("id", "image_tag", "username", "first_name", "last_name")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)

    # userni qo'shishda ko'rsatiladigan fieldsetlar
    fieldsets = (
        (None, {"fields": ("username", "password", "image")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "phone")}),
        (_("Role"), {"fields": ("role",)}),
        (_("Permissions"), {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
        }),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # yangi user yaratishda ishlatiladigan fieldlar
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "first_name", "last_name", "role", "phone", "password",),
        }),
    )

