from datetime import timezone

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
    def duration(self):
        if self.updated_at is not None:
            return self.updated_at - self.created_at
        return timezone.now() - self.created_at


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

    #precisa de uma função que pegue o valor(price_hour) no parking_spot
    # e multiplique pelo tempo de duração (duration)
    total_value = models.FloatField(
        db_column='total_value',
        null=False,
        default=0.0,
    )

    def save(self, *args, **kwargs):
        """Override o método save para calcular o valor total automaticamente."""
        self.total_value = self.id_parking_spot.calculate_total_value()
        super().save(*args, **kwargs)
