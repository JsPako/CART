from django.contrib import admin
from .models import Profile, Vehicle, Part, Modification, Requirement, Stage, Fix, Repair

admin.site.register(Profile)
admin.site.register(Vehicle)
admin.site.register(Part)
admin.site.register(Modification)
admin.site.register(Requirement)
admin.site.register(Stage)
admin.site.register(Fix)
admin.site.register(Repair)