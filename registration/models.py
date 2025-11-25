from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    gender = models.CharField(max_length=12)
    password = models.CharField(max_length=150)
    date_registered = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(
        upload_to = 'profile_picture/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    