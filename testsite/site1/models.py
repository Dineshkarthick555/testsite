from django.db import models

# Create your models here.

class Pytest(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    age=models.IntegerField()
    class Meta:
        db_table="Pytest"
        