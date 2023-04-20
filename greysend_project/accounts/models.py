# from django.db import models
from django.contrib.auth import models

# Create your models here.
class AccountUser(models.User):
    # given_name = models.CharField(max_length=50)
    # family_name = models.CharField(max_length=50)
    # user_name = models.CharField(max_length=50, unique=True)
    # password = models.CharField(max_length=50)

    def __str__(self):
        return self.username