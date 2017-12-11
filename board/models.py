from django.db import models as db_models
from django.conf import settings

MAX_SUBJECT_LENGTH = 256


class Message(db_models.Model):
    author = db_models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=db_models.CASCADE, null=True)
    datetime = db_models.DateTimeField(null=False)
    subject = db_models.CharField(null=False, max_length=MAX_SUBJECT_LENGTH)
    body = db_models.TextField(null=False)
    image = db_models.ImageField(null=True)

    def get_author(self):
        return self.author.get_username() if self.author else "anonymous"
