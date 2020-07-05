from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination} in {self.duration}"

class Passenger(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passenger")

    def __str__(self):
        return f"{self.first} {self.last}"
