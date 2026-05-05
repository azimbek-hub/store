from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
USER_TYPE_CHOICES = (
     ('VENDOR', 'VENDOR'),
     ('CUSTOMER', 'CUSTOMER'),
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email.split('@')[0]
        super(CustomUser, self).save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField()
    phone_number = models.CharField(max_length=11, blank=True)
    user_type = models.CharField(choices=USER_TYPE_CHOICES, default='CUSTOMER', max_length=10)
    # currency = models.ForeignKey('Currency', on_delete=models.PROTECT)

    def __str__(self):
        if self.user.is_authenticated:
            if self.full_name:
                return self.full_name.split(' ')[0]
            return self.user.username
        else:
            return self.user.username
