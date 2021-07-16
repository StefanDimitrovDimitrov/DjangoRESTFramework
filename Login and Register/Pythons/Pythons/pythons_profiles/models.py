from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

from django.db import models

UserModel = get_user_model()


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(
        max_length=20
    )
    last_name = models.CharField(
        max_length=20
    )
    age = models.IntegerField()
    profile_image = models.ImageField(
        upload_to='profile',
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
