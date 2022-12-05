import uuid
from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.shortcuts import reverse


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Position(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    price = models.FloatField(null=False, blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Position Product: {self.product.name} | Created On: {self.created_at.strftime('%d-%m-%Y')}"


class Sale(BaseModel):
    transaction_id = models.CharField(max_length=12, null=False, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sales_person = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = str(uuid.uuid4()).replace("-", "")[:12]
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(viewname='sales:sale_detail_view', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Sale: {self.transaction_id} | Created On: {self.created_at.strftime('%d-%m-%Y')}"


class CSV(BaseModel):
    filename = models.CharField(max_length=120, null=True)
    csv_file = models.FileField(upload_to="csvs", null=True)

    def __str__(self):
        return f"CSV FileName: {self.filename}"
