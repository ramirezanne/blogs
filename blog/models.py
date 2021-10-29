from django.db import models

# Create your models here.
class blog(models.Model):
    name = models.CharField(verbose_name="Blog name", max_length=200)
    content = models.CharField(verbose_name="Blog content", max_length=5000000)
    comment = models.CharField(verbose_name="Blog comment", max_length=200, default="")
    author = models.CharField(verbose_name="Blog author", max_length= 30, default="")

def __str__(self):
        return "%s" %self.name
