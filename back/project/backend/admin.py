from django.contrib import admin
from .models import User as CustomUser, ChatRoom, Message

# Register your custom models
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)

admin.site.register(ChatRoom)
admin.site.register(Message)
