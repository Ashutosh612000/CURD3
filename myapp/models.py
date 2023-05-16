from django.db import models



# Create your models here.

class Myapp_Detail(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    age = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = ("app1")

