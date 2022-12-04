from django.db import models
from profiles.models import Profile


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Report(BaseModel):
    name = models.CharField(max_length=120, null=False, blank=False)
    image = models.ImageField(upload_to='reports', null=True)
    remark = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Report: {self.name} | Created On: {self.created_at.strftime('%d-%m-%Y')}"
