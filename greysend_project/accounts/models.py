from django.db import models

# Create your models here.
class ChatUser(models.Model):
    given_name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name