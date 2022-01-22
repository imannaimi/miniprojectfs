from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Create your models here.
#on_delete CASCADE if you delete the id all the data related to id will be deleted
#blank=true (so if people don't fill anything there you won't receive an error)
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.TextField(blank=True)
    hobby = models.TextField(blank=True)
    company = models.TextField(blank=True)

    def __str__ (self):
        return self.user.username