from django.db import models
from django.utils.timezone import now



# Create your models here.
class Message(models.Model):
    message = models.TextField()
    createdon = models.DateTimeField(default=now, editable=False)

