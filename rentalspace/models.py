from django.db import models

class VansModel(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    body_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.make + ' ' + self.model or ''

