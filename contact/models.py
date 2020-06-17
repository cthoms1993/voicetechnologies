from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, help_text="name of sender")
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "feedback"

    def __str__(self):
        return self.name + "-" + self.email
