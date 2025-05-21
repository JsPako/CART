from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=128)

    def __str__(self):
        return f"USER DISPLAY NAME {self.display_name}"


class Vehicle(models.Model):
    registration = models.CharField(max_length=8, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    year = models.IntegerField()
    nickname = models.CharField(max_length=128)

    def __str__(self):
        return f"VEHICLE REGISTRATION {self.registration}"


class Part(models.Model):
    CATEGORIES = [
        ("ENGINE", "Engine"),
        ("TRANSMISSION", "Transmission"),
        ("GASKET", "Gaskets, and Sealing"),
        ("DRIVE", "Drive System"),
        ("SUSPENSION", "Suspension, Damping, and Steering"),
        ("BRAKE", "Brakes"),
        ("ELECTRIC", "Electrics, and Electronics"),
        ("EXHAUST", "Exhaust Systems"),
        ("BODY", "Body, and Exterior"),
        ("INTERIOR", "Interior, and Comfort"),
        ("MISC", "Fasteners, and Miscellaneous"),
        ("TYRES", "Tyres and related products")]

    number = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=12, choices=CATEGORIES)
    source = models.URLField(max_length=256)
    cost = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return f"PART ID {self.number}, SOURCED FROM {self.source}"


class Modification(models.Model):
    number = models.CharField(max_length=24, unique=True)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    amount = models.IntegerField()
    completion = models.BooleanField()

    def __str__(self):
        return f"MODIFICATION ID {self.number}"


class Requirement(models.Model):
    number = models.CharField(max_length=24, unique=True)
    modification = models.ForeignKey(Modification, on_delete=models.CASCADE)
    required = models.ManyToManyField(Modification, related_name='requirements')

    def __str__(self):
        return f"REQUIREMENT ID {self.number}"


class Stage(models.Model):
    number = models.CharField(max_length=24, unique=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    modifications = models.ManyToManyField(Modification, related_name='stages')
    completion = models.BooleanField()

    def __str__(self):
        return f"STAGE ID {self.number}"


class Fix(models.Model):
    number = models.CharField(max_length=24, unique=True)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        verbose_name_plural = "Fixes"

    def __str__(self):
        return f"FIX ID {self.number}"


class Repair(models.Model):
    CATEGORIES = [
        ("MAINTAIN", "Maintenance, and Service"),
        ("REPAIR", "Repairs")]
    number = models.CharField(max_length=24, unique=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    fixes = models.ManyToManyField(Fix, related_name='repairs')
    name = models.CharField(max_length=128)
    description = models.TextField()
    category = models.CharField(max_length=8, choices=CATEGORIES)
    completion = models.BooleanField()

    def __str__(self):
        return f"REPAIR ID {self.number}"
