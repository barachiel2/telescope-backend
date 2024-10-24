from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolios', blank=True, null=True)
    geographic_region = models.CharField(max_length=255, default='Unknown Region')
    description = models.TextField(blank=True)
    location = models.PointField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='properties')
    address = models.CharField(max_length=255)
    estimated_value = models.DecimalField(max_digits=12, decimal_places=2)
    construction_year = models.IntegerField()
    square_footage = models.DecimalField(max_digits=10, decimal_places=2)
    representational_image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address
