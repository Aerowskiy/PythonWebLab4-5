from django.contrib import admin
from .models import Deal, Review


@admin.register(Deal)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'performer', 'completed')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'rating', 'user', 'reviewer')

