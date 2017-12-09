from django.db import models as db_models
from django.contrib.auth import models as auth_models

MAX_SUBJECT_LENGTH = 256


class Message(db_models.Model):
    author = db_models.ForeignKey(auth_models.User, on_delete=db_models.CASCADE, null=True)
    datetime = db_models.DateTimeField(null=False)
    subject = db_models.CharField(null=False, max_length=MAX_SUBJECT_LENGTH)
    body = db_models.TextField(null=False)
    # https://docs.djangoproject.com/en/1.11/ref/models/fields/#imagefield
    image = db_models.ImageField(null=True)

    def get_author(self):
        return self.author.get_username() if self.author else "anonymous"
