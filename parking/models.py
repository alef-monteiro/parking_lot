from django.utils import timezone

from django.db import models


# Create your models here.

class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
    )

    active = models.BooleanField(
        db_column='active',
        null=False,
        default=False,
    )

    created_at = models.DateField(
        db_column='created_at',
        null=False,
        auto_now_add=True,
    )

    updated_at = models.DateField(
        db_column='updated_at',
        null=False,
        auto_now=True,
    )

    class Meta:
        managed = True
        abstract = True


class Client(ModelBase):
    name = models.CharField(
        db_column='name',
        null=False,
        max_length=70,
    )
    cpf = models.CharField(
        db_column='cpf',
        null=False,
        max_length=12,
    )
    phone_number = models.CharField(
        db_column='phone_number',
        null=False,
        max_length=11,
    )


class Vehicle(ModelBase):
    id_client = models.ForeignKey(
        Client,
        db_column='id_client',
        null=False,
        on_delete=models.CASCADE,
    )

    license_plate = models.CharField(
        db_column='license_plate',
        null=False,
        max_length=10,
    )
    car_model = models.CharField(
        db_column='car_model',
        null=False,
        max_length=10,
    )
    colour = models.CharField(
        db_column='colour',
        null=False,
        max_length=10,
    )

    vehicle_type = models.CharField(
        db_column='vehicle_type',
        null=False,
        max_length=10,
    )


class ParkingSpot(ModelBase):
    price_hour = models.FloatField(
        db_column='price_hour',
        null=False,
    )
    id_vehicle = models.ForeignKey(
        Vehicle,
        db_column='id_vehicle',
        null=False,
        on_delete=models.CASCADE,
    )


class Transaction(ModelBase):
    id_client = models.ForeignKey(
        Client,
        db_column='id_client',
        null=False,
        on_delete=models.CASCADE,
    )
    id_vehicle = models.ForeignKey(
        Vehicle,
        db_column='id_vehicle',
        null=False,
        on_delete=models.CASCADE
    )
    id_parking_spot = models.ForeignKey(
        ParkingSpot,
        db_column='id_parking_spot',
        null=False,
        on_delete=models.CASCADE
    )
    check_in = models.DateTimeField(
        db_column='check_in',
        null=False,
        auto_now_add=True,  # Inicio
    )
    check_out = models.DateTimeField(
        db_column='check_out',
        null=False,
        auto_now=True,  # Fim
    )
    total_value = models.FloatField(
        db_column='total_value',
        null=False,
        default=0.0,
    )

    def duration(self):
        if self.check_out is None:
            return timezone.now() - self.check_in
        return self.check_out - self.check_in

    def calculate_total(self):
        duration = self.duration()
        hours = duration.total_seconds()
        price_hour = self.id_parking_spot.price_hour
        total = price_hour * hours
        return total

    def save(self, *args, **kwargs):
        if self.check_out:
            self.total_value = self.calculate_total()
        super().save(*args, **kwargs)
