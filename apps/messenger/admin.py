from django.contrib import admin
from .models import MessengerUser


@admin.register(MessengerUser)
class AdminMessengerUser(admin.ModelAdmin):
    list_display = (
        'user_id',
        'first_name',
        'last_name',
        'gender',
        'timezone',
        'image',
        'date',
    )
    
    class Meta:
        model = MessengerUser
