from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=120, null=False, blank=False)
    price = models.FloatField(help_text='Amount in Rs.', null=False, blank=False)
    image = models.ImageField(upload_to="products", default="no_picture.png")

    def __str__(self):
        return f"Product: {self.name} | Created On: {self.created_at.strftime('%d-%m-%Y')}"
