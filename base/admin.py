from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User, Securities_type, Securities

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Securities_type)
admin.site.register(Securities)
