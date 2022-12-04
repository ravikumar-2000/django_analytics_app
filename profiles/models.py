from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio yet ....!")
    avatar = models.ImageField(upload_to="avatars", default="no_picture.png")

    def __str__(self):
        return f"Profile: {self.user.username} | Created on: {self.created_at.strftime('%d-%m-%Y')}"
