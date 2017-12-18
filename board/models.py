from django.db import models
from django.conf import settings

MAX_SUBJECT_LENGTH = 256


class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(null=False)
    subject = models.CharField(null=False, max_length=MAX_SUBJECT_LENGTH)
    body = models.TextField(null=False)
    image = models.ImageField(null=True)
    is_edited = models.BooleanField(default=False)

    def get_author(self):
        return self.author.get_username() if self.author else "anonymous"

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()

        return super().delete(*args, **kwargs)
