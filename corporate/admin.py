from django.contrib import admin

# Register your models here.
from .models import (Corporate,Items,CorperateGroup, ContactModel)


admin.site.register(Corporate)

admin.site.register(Items)
admin.site.register(CorperateGroup)
admin.site.register(ContactModel)
