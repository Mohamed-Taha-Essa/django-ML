from django.db import models

# Create your models here.
class Iris(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    result = models.CharField(max_length=50 ,null=True ,blank=True)

    def __str__(self):
        return f"{self.result}"