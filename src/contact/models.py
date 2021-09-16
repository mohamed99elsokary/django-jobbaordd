from django.db import models

# Create your models here.
class Info(models.Model):
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    working_days = models.CharField(max_length=100, blank=True, null=True)
    working_time = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
