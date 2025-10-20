from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} {self.country}'

class Material(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class Yarn(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    weight = models.FloatField(default=50.0, help_text="weight")
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='yarns',null=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, related_name='yarns')
    def __str__(self):
        return f'{self.name} {self.material} {self.brand_id} {self.price} {self.weight}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    def __str__(self):
        return f'{self.name} {self.price}'
















# Create your models here.
