from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_citizen = models.BooleanField('Is citizen', default=False)
    is_committee = models.BooleanField('Is committee', default=False)
    is_securityguard = models.BooleanField('Is committee', default=False)

