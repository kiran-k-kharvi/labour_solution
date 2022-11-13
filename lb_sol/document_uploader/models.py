from user_auth.models import User
from django.db import models


class Document(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    document = models.FileField()
