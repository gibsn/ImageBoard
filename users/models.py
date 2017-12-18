from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(null=False)
    image = models.ImageField(null=True)

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()

        return super().delete(*args, **kwargs)
