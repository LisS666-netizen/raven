from django.contrib import admin
from .models import ATSUser, Position, Division, VController, Gender


admin.site.register(ATSUser)
admin.site.register(Position)
admin.site.register(Division)
admin.site.register(VController)
admin.site.register(Gender)