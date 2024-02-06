from django.db import models

# Create your models here.
class soat(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self.name
    