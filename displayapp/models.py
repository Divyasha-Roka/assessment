from django.db import models

# Create your models here.
class Display(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.ImageField(upload_to='images' , blank=False)