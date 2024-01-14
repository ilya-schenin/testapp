from django.db import models
from user.models import CustomUser


class Message(models.Model):
    user1 = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='user1')
    user2 = models.ForeignKey(CustomUser, on_delete=models.PROTECT,  related_name='user2')
    message = models.TextField(max_length=500)
