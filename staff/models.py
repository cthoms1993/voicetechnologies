from django.db import models


# Create your models here.
class StaffMember(models.Model):
    name = models.CharField(max_length=254, default='')
    title = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images', default='')

    def __str__(self):
        return self.name
